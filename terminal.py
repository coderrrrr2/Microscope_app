from backend.utils import calculate_actual_size
from backend.models import save_specimen, create_table

create_table()

username = input("Enter username: ")
microscope_size = float(input("Enter microscope size (mm): "))
magnification = float(input("Enter magnification: "))

actual_size = calculate_actual_size(microscope_size, magnification)
save_specimen(username, microscope_size, magnification, actual_size)

print(f"Actual size: {actual_size:.2f} mm")
