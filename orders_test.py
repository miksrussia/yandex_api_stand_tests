# Сергей Горячев, 11-я когорта — Финальный проект. Инженер по тестированию плюс
import sendor_stand_request
import data

# def positive_assert_of_create_order_and_save_track(body):
#     order_response = sendor_stand_request.post_new_order(body)
#     assert order_response.status_code == 201
#     assert order_response.json() != ""

# def positive_assert_of_create_order_and_save_track_order_by_number(order_track):
#     order_number_response = sendor_stand_request.get_order_by_number(order_track)
#     assert order_number_response.status_code == 200
#     assert order_number_response.json() != ""

# def test_create_order():
#     positive_assert_of_create_order_and_save_track(data.order_body)

# def test_create_order_info():
#     positive_assert_of_create_order_and_save_track_order_by_number(data.order_track)

# response = sendor_stand_request.post_new_order(data.order_body)

def test_positive_assert_of_create_order():
    create_order_response = sendor_stand_request.post_new_order(data.order_body)
    assert create_order_response.status_code == 201

    order_track = str(create_order_response.json()['track'])
    order_number_response = sendor_stand_request.get_order_by_number(order_track)
    assert order_number_response.status_code == 200


# positive_assert_of_create_order(data.order_body)
# print(order_response.status_code)
# print(order_response.json())

