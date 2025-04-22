
from backend.models import save_specimen, create_table

def calculate_actual_size(microscope_size, magnification):
    if magnification == 0:
        raise ValueError("Magnification cannot be zero.")
    return microscope_size / magnification


username = input("Enter username: ")
microscope_size = float(input("Enter microscope size (mm): "))
magnification = float(input("Enter magnification: "))

actual_size = calculate_actual_size(microscope_size, magnification)


print(f"Actual size: {actual_size:.2f} mm")





