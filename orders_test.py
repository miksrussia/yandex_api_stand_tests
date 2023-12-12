# Сергей Горячев, 11-я когорта — Финальный проект. Инженер по тестированию плюс
import sendor_stand_request
import data



def test_positive_assert_of_create_order():
    create_order_response = sendor_stand_request.post_new_order(data.order_body)
    assert create_order_response.status_code == 201
    order_track = str(create_order_response.json()['track'])
    order_number_response = sendor_stand_request.get_order_by_number(order_track)
    assert order_number_response.status_code == 200




