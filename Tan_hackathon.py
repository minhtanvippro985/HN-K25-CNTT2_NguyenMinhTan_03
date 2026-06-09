customer_list = [
    {
        "customer_id" : "KH001",
        "customer_name" : "Tran Minh Cuong",
        "phone_number" : "0987654321",
        "total_paid" : 12_500_000,
        "buy_count" : 5,
        "ratio" : 5,
        "membership_rank" : "Vàng"
    }

]


def display_customer_list(list_here):
    if len(list_here) == 0:
        print("Danh sách hiện đang trông")
    else:
        print(f"{'Mã':<10} | {'Tên' :<20} | {'Số diện thoại' :<12} | {'Tổng chi tiêu (VND)':<10} | {'Số lần mua hàng ':<5} | {'Chiết khẩu':<5} | {'Hạng':<5}")
        for people in list_here:
            print(f"{people['customer_id']:<10} | {people['customer_name'] :<20} | {people['phone_number'] :<13} | {people['total_paid']:<20} | {people['buy_count']:<15} | {people['ratio']:<7} % | {people['membership_rank']:<6}")

def customer_in_list_check(customer_id_input , list_here):
    found = False
    for index , people in enumerate(list_here, start=0):
        if people['customer_id'] == customer_id_input:
            found = True
            return people
    if found == False:
        return None

def validate_number(number_input):
    if number_input < 0 :
        return False
    else:
        return True

def calculate_ratio_rank(input_paid):
    if input_paid >= 15_000_000 and input_paid < 30_000_000:
        return "Vàng",5
    elif input_paid >= 5_000_000 and input_paid < 15_000_000:
        return "Bạc",2
    elif input_paid >= 30_000_000:
        return "Kim cương",10
    else:
        return "Đồng",0

def add_new_customer(list_here):
    new_customer_id_input = input("Nhập mã khách hàng mới : ").strip().upper()
    if new_customer_id_input == "":
        print("Mã khách hàng không được để trống!")
        return
    found_people = customer_in_list_check(new_customer_id_input , list_here)
    if not found_people == None:
        print(f"{new_customer_id_input} Đã tồn tại trong hệ thống rồi!")
        return
    new_customer_name = input("Nhập tên khách hàng mới : ").strip().title()
    if new_customer_name == "":
        print("Tên khách hàng không được để trống")
        return
    new_phone_number = input("Nhập số điện thoại mới : ").strip()
    if new_phone_number == "":
        print("Số điện thoại không được để trống!")
    if new_phone_number.isdigit() == False:
        print("Số điện thoại không được có ký tự..")
        return
    if len(new_phone_number) != 10:
        print("Số điện thoại chỉ có 10 chữ số")
        return
    try:
        new_total_paid = int(input("Nhập tổng chi tiêu ban đầu : "))
    except ValueError:
        print("Nhập sai định dạng!")
        return
    if validate_number(new_total_paid) == False:
        print("Số nhập vào phải là một số >= 0!")
        return
    try:
        new_boughts = int(input("Nhập Số lần mua hàng : "))
    except ValueError:
        print("Nhập sai định dạng!")
        return
    if validate_number(new_boughts) == False:
        print("Số nhập vào phải là một số >= 0!")
        return
    rank,ratio_cal = calculate_ratio_rank(new_total_paid)
    new_customer = {
        "customer_id" : new_customer_id_input,
        "customer_name" : new_customer_name,
        "phone_number" : new_phone_number,
        "total_paid" : new_total_paid,
        "buy_count" : new_boughts,
        "ratio" : ratio_cal,
        "membership_rank" : rank
    }
    print(f"Đã thêm khách hàng thành công! {new_customer_id_input}")
    list_here.append(new_customer)
    
def update_customer(list_here):
    input_update_id = input("Nhập mã khách hàng cần cập nhật : ").strip().upper()
    if input_update_id == "":
        print("Dữ liệu cần cập nhật vào không được để trống")
        return
    if customer_in_list_check(input_update_id,list_here) == None:
        print(f"Không tìm thấy {input_update_id} trong danh sách!")
    else:
        people_dict = customer_in_list_check(input_update_id,list_here)
        print(f"Đã tìm thấy {input_update_id} trong danh sách!")
        update_phone_num = input("Nhập số điện thoại mới : ").strip()
        if update_phone_num == "":
            print("Số điện thoại không được để trống!")
        if update_phone_num.isdigit() == False:
            print("Số điện thoại không được có ký tự..")
            return
        if len(update_phone_num) != 10:
            print("Số điện thoại chỉ có 10 chữ số")
            return
        try:
            update_total_paid = int(input("Nhập tổng chi tiêu ban đầu : "))
        except ValueError:
            print("Nhập sai định dạng!")
            return
        if validate_number(update_total_paid) == False:
            print("Số nhập vào phải là một số >= 0!")
            return
        try:
            update_boughts = int(input("Nhập Số lần mua hàng : "))
        except ValueError:
            print("Nhập sai định dạng!")
            return
        if validate_number(update_boughts) == False:
            print("Số nhập vào phải là một số >= 0!")
            return
        new_rank,new_ratio_cal = calculate_ratio_rank(update_total_paid)
        people_dict.update({
             "phone_number" : update_phone_num,
             "total_paid" : update_total_paid,
             "buy_count" : update_boughts,
             "ratio" : new_ratio_cal,
             "membership_rank" : new_rank
        })
        print(f"Đã cập nhật thành công cho khách hàng {input_update_id}")

def delete_customer(list_here):
    input_delete_find = input("Nhập ID khách hàng mà bạn muốn xóa : ").strip().upper()
    if input_delete_find == "":
        print("Không được để trống!")
    if not customer_in_list_check(input_delete_find,list_here) == None:
        person_info = customer_in_list_check(input_delete_find,list_here)
        while True:
            small_choice = input(f"Bạn có chắc muốn xóa khách hàng {person_info['customer_name']}\ny.Có\nn.Không\nLua chon của bạn : ").lower().strip()
            if small_choice == "y":
                print(f"Đã xóa thành công khách hàng {input_delete_find} ")
                list_here.remove(person_info)
                return
            elif small_choice == "n":
                print("Đã hủy xóa khách hàng")
                return
            else:
                print("Vui lòng chọn đúng chức năng")
    else:
        print(f"Không tìm thấy {input_delete_find} trong danh sách!")

def find_customer_by_id(list_here):
    input_customer_find = input("Nhập mã khách hàng bạn muốn tìm :").strip().upper()
    if input_customer_find == "":
        print("Không được để trống!")
        return
    if not customer_in_list_check(input_customer_find,list_here) == None:
        person_info = customer_in_list_check(input_customer_find,list_here)
        print(f"Mã {person_info['customer_id']:<10} | Tên {person_info['customer_name'] :<20} | SĐT {person_info['phone_number'] :<13} | Tích lũy {person_info['total_paid']:<20} | lần mua {person_info['buy_count']:<15} | Ưu đãi {person_info['ratio']:<7} % | Hạng {person_info['membership_rank']:<6}")
    else:
        print(f"Không tìm thấy {input_customer_find} trong danh sách!")

def find_customer_by_name(list_here):
    input_name_find = input("Nhập tên khách mà bạn muốn tìm : ").strip().lower()
    if input_name_find == "":
        print("Không được để trống!")
        return
    count_search = 0
    for people in list_here:
        if people['customer_name'].lower() == input_name_find or people['customer_name'].lower().count(input_name_find):
            count_search = count_search + 1
            print(f"Mã {people['customer_id']} | Tên {people['customer_name']} | SĐT {people['phone_number']} | Tích lũy {people['total_paid']} | lần mua {people['buy_count']} | Ưu đãi {people['ratio']} % | Hạng {people['membership_rank']}")
    if count_search == 0:
        print("Không tìm thấy kết quả nào phù hợp!")
    else:
        print("=====================================================================")
        print(f"Đã tìm thấy {count_search} kết quả phù hợp của {input_name_find} !")

def statistics_by_ranks(list_here):
    count_copper = 0
    count_silver = 0
    count_gold = 0
    count_diamond = 0
    for people in list_here:
        if people['membership_rank'] == "Kim cương":
            count_diamond = count_diamond + 1
        elif people['membership_rank'] == "Bạc":
            count_silver = count_silver + 1
        elif people['membership_rank'] == "Vàng":
            count_gold = count_gold + 1
        else:
            count_copper = count_copper + 1
    print(f"""
======== THỐNG KÊ PHÂN HẠNG THÀNH VIÊN ==========
Đồng : {count_copper} KH
Bạc :  {count_silver} KH
Vàng : {count_gold} KH
Kim Cương : {count_diamond} KH
=================================================

""")

while True:
    choice = input("""
=========================================
1. Hiển thị danh sách khách hàng
2. Đăng ký khách hàng mới
3. Cập nhật thông tin giao dịch
4. Xóa dữ liệu khách hàng
5. Tìm kiếm khách hàng
6. Thống kê phân hạng thành viên
7. Thoát chương trình
==========================================
Nhập lựa chọn của bạn ....  
""").strip()
    match choice:
        case "7":
            print("Thoát chương trình...")
            break
        case "1":
            display_customer_list(customer_list)
        case "2":
            add_new_customer(customer_list)
        case "3":
            update_customer(customer_list)
        case "4":
            delete_customer(customer_list)
        case "5":
            while True:
                small_menu = input("Nhập chức năng tìm kiếm theo \n1.Theo mã KH\n2.Theo tên gần đúng của khách hàng\n0.Thoát về menu chính..\nLựa chọn của bạn.. : ")
                match small_menu:
                    case "1":
                        find_customer_by_id(customer_list)
                    case "2":
                        find_customer_by_name(customer_list)
                    case "0":
                        print("Thoát về menu chính...")
                        break
                    case _:
                        print("Vui lòng chọn 1 , 2 hoặc 0...")
        case "6":
            statistics_by_ranks(customer_list)
        case _:
            print("Vui lòng chỉ chọn từ 1 - 7")