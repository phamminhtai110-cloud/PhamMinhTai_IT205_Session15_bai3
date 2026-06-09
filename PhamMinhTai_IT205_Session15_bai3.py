available_seats = 50
flight_revenue = 0.0
BASE_PRICE = 2000.0


def calculate_ticket_price(quantity: int, seat_class: int) -> float:
    """
    Calculate total ticket price.
    param: quantity (int), seat_class (int)
    return: float
    """
    if seat_class == 1:
        price = BASE_PRICE
    elif seat_class == 2:
        price = BASE_PRICE * 1.5
    else:
        return -1

    subtotal = quantity * price
    service_fee = subtotal * 0.05
    return subtotal + service_fee


def process_booking(quantity, seat_class, total_price):
    global available_seats, flight_revenue

    if quantity > available_seats:
        print(f"Rất tiếc, chuyến bay chỉ còn {available_seats} chỗ trống.")
        return False

    available_seats -= quantity
    flight_revenue += total_price

    print("--- ĐẶT VÉ MÁY BAY ---")
    print(f"Số lượng: {quantity} | Hạng: {'Economy' if seat_class == 1 else 'Business'}")
    print(f"Tổng thanh toán: ${total_price}")
    print(f"Đặt vé thành công! Ghế trống còn lại: {available_seats}")
    return True


def cancel_ticket(quantity):
    global available_seats, flight_revenue

    if quantity <= 0:
        print("Dữ liệu không hợp lệ")
        return 0

    if available_seats + quantity > 50:
        print("Lỗi: Số lượng vé hủy vượt quá số vé đã bán ra.")
        return 0

    refund_per_ticket = BASE_PRICE * 0.8
    total_refund = refund_per_ticket * quantity

    available_seats += quantity
    flight_revenue -= total_refund

    print("--- HỦY VÉ & HOÀN TIỀN ---")
    print(f"Hủy vé thành công. Hệ thống đã hoàn lại: ${total_refund} (80% giá cơ bản).")
    print(f"Ghế trống hiện tại: {available_seats}")

    return total_refund


def print_flight_status():
    """
    Print flight report status
    """
    print("--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print(f"Sức chứa tối đa: 50")
    print(f"Ghế đã đặt: {50 - available_seats}")
    print(f"Ghế trống: {available_seats}")
    print(f"Tổng doanh thu hiện tại: ${flight_revenue}")


def main():
    while True:
        print("\n============= SKYBOOKING SYSTEM =============")
        print("Chuyến bay: VN2026 | Khởi hành: Hà Nội")
        print("1. Đặt vé máy bay")
        print("2. Hủy vé & Hoàn tiền")
        print("3. Xem tình trạng chuyến bay")
        print("4. Đóng hệ thống")

        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            try:
                quantity = int(input("Nhập số lượng vé: "))
                seat_class = int(input("Chọn hạng vé (1: Economy, 2: Business): "))

                if quantity <= 0 or seat_class not in [1, 2]:
                    print("Dữ liệu không hợp lệ")
                    continue

                if quantity > available_seats:
                    print(f"Rất tiếc, chuyến bay chỉ còn {available_seats} chỗ trống.")
                    continue

                total_price = calculate_ticket_price(quantity, seat_class)

                print("--- ĐẶT VÉ MÁY BAY ---")
                print(f"Số lượng: {quantity} | Hạng: {'Economy' if seat_class == 1 else 'Business'}")
                print(f"Tổng thanh toán: ${total_price}")

                process_booking(quantity, seat_class, total_price)

            except:
                print("Dữ liệu không hợp lệ")

        elif choice == "2":
            try:
                quantity = int(input("Nhập số lượng vé muốn hủy: "))
                cancel_ticket(quantity)
            except:
                print("Dữ liệu không hợp lệ")

        elif choice == "3":
            print_flight_status()

        elif choice == "4":
            print("Cảm ơn quý khách đã sử dụng hệ thống!")
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()