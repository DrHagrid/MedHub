# -*- coding: utf-8 -*-
import re, random
from django.shortcuts import render
from django.http import JsonResponse
from user.views import create_user_info
from content.models import *
from test.models import *
from user.models import *


def test_page(request, unit, group, test_id):
    created = create_user_info(request)  # Создать информацию о пользователе, в случае её отсутствия

    unit = unit_list[unit]
    group = unit['group'].objects.get(variable=group)

    if 'lat_' in test_id:
        type = re.split('lat_', test_id)[1]
        type = unit['type'].objects.get(variable=type)
        element = unit['model'].objects.filter(group=group).filter(type=type)[0]
        element_id = element.id
        title = 'Тест по латинским терминам'
        total = len(unit['model'].objects.filter(group=group).filter(type=type))

        test_type = 'input'
    else:
        element = Test.objects.get(pk=test_id).questions.all()[0]
        element_id = element.id
        title = Test.objects.get(pk=test_id).name
        total = len(Test.objects.get(pk=test_id).questions.all())

        test_type = element.test_type
        options = element.options.split(';')
        random.shuffle(options)

    data = {'test_type': test_type, 'unit': unit['variable'], 'group': group.variable, 'test_id': test_id,
            'element_id': element_id}

    if 'lat_' in test_id:
        return render(request, 'test/test_lat.html', locals())
    else:
        return render(request, 'test/test.html', locals())


def test_data(request):
    return_dict = dict()
    data = request.POST

    action = data.get("action")
    test_type = data.get("test_type")
    unit = data.get("unit")
    group = data.get("group")
    test_id = data.get("test_id")
    if 'lat_' in test_id:
        type = re.split('lat_', test_id)[1]
    element_id = data.get("element_id")
    answer = data.get("answer")
    start = data.get("start")

    unit = unit_list[unit]
    group = unit['group'].objects.get(variable=group)
    if 'lat_' in test_id:
        type = unit['type'].objects.get(variable=type)

    if action == 'check':
        if 'lat_' in test_id:
            element = unit['model'].objects.get(pk=element_id)
            initial = element.lat_term.lower().split(' ')
            elements_selection = unit['model'].objects.filter(group=group).filter(type=type)
        else:
            element = Question.objects.get(pk=element_id)
            initial = element.answer.lower().split(' ')
            elements_selection = Test.objects.get(pk=test_id).questions.all()

        entrance = answer.lower().split(' ')
        intersection = list(set(initial) & set(entrance))
        if (len(entrance) == len(initial)) and (len(entrance) == len(intersection)):  # При условии верного ответа
            elements_id = list()
            for e in elements_selection:
                elements_id.append(e.id)
            elements_id.sort()
            for e in elements_id:
                if e > int(element_id):
                    next_element_id = e
                    break
                else:
                    next_element_id = 0

            response = 'True'

            if next_element_id != 0:
                if not ('lat_' in test_id):
                    return_dict["next_test_type"] = Question.objects.get(pk=next_element_id).test_type
                else:
                    return_dict["next_test_type"] = 'input'
            return_dict["next_element_id"] = next_element_id
        else:
            response = 'False'

        # Если пользователь зарегистрирован, то сохранить статистику
        if request.user.is_authenticated:
            user_info = UserInfo.objects.get(user=request.user)

            if user_info.data:
                user_data = user_info.get_data()
            else:
                user_data = dict()

            if start == 'true':
                user_data[unit['variable'] + "_" + group.variable + "_" + test_id] = {'correct': 0, 'incorrect': 0, 'incorrect_list': []}

            if response == 'True':
                if not any(element_id in el for el in user_data[unit['variable'] + "_" + group.variable + "_" + test_id]['incorrect_list']):
                    user_data[unit['variable'] + "_" + group.variable + "_" + test_id]['correct'] += 1
            else:
                if not any(element_id in el for el in user_data[unit['variable'] + "_" + group.variable + "_" + test_id]['incorrect_list']):
                    user_data[unit['variable'] + "_" + group.variable + "_" + test_id]['incorrect'] += 1
                    user_data[unit['variable'] + "_" + group.variable + "_" + test_id]['incorrect_list'].append(element_id)
            user_info.set_data(user_data)
            user_info.save(force_update=True)

        return_dict["response"] = response
    elif action == 'next':
        if 'lat_' in test_id:
            element = unit['model'].objects.get(pk=element_id)
            return_dict["test_type"] = 'input'
            return_dict["answer"] = element.lat_term
            return_dict["title"] = element.name
            if element.image:
                return_dict["image_url"] = '../../../../../' + element.image

        else:
            element = Question.objects.get(pk=element_id)
            return_dict["test_type"] = element.test_type
            return_dict["answer"] = element.answer
            return_dict["title"] = element.question
            if element.image:
                return_dict["image_url"] = '../../../../../' + element.image

            if test_type == 'radio':
                options = element.options.split(';')
                random.shuffle(options)
                options_html = ''
                for option in options:
                    options_html += \
                                    '<div class="form-check form-check-radio text-left"> \
                                        <label class="form-check-label"> \
                                            <input class="form-check-input" type="radio" name="test" value="' + option + '"> \
                                            ' + option + ' \
                                            <span class="circle"> \
                                                <span class="check"></span> \
                                            </span> \
                                        </label> \
                                    </div>'
                return_dict["options_html"] = options_html

    return JsonResponse(return_dict)


def stat_page(request, unit, group, test_id):
    created = create_user_info(request)  # Создать информацию о пользователе, в случае её отсутствия

    unit = unit_list[unit]
    group = unit['group'].objects.get(variable=group)
    if 'lat_' in test_id:
        test_name = 'Тест по латинским терминам'
    else:
        test_name = Test.objects.get(pk=test_id).name

    # Если пользователь зарегистрирован, то загрузить статистику
    if request.user.is_authenticated:
        user_info = UserInfo.objects.get(user=request.user)
        user_data = user_info.get_data()

        if not (unit['variable'] + "_" + group.variable + "_" + test_id in user_data.keys()):
            user_data[unit['variable'] + "_" + group.variable + "_" + test_id] = {'correct': 0, 'incorrect': 0,
                                                                                  'incorrect_list': []}

        if 'lat_' in test_id:
            element_class = unit['model']
            type = re.split('lat_', test_id)[1]
            type = unit['type'].objects.get(variable=type)
            total = len(unit['model'].objects.filter(group=group).filter(type=type))
        else:
            element_class = Question
            total = len(Test.objects.get(pk=test_id).questions.all())

        correct = user_data[unit['variable'] + "_" + group.variable + "_" + test_id]['correct']
        incorrect = user_data[unit['variable'] + "_" + group.variable + "_" + test_id]['incorrect']
        incorrect_list = list()
        for e in user_data[unit['variable'] + "_" + group.variable + "_" + test_id]['incorrect_list']:
            incorrect_list.append(element_class.objects.get(pk=e))

        correct_percent = round((int(correct) / total) * 100)
        incorrect_percent = 100 - correct_percent

    return render(request, 'test/stat.html', locals())
