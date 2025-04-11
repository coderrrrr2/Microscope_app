def calculate_actual_size(microscope_size, magnification):
    if magnification == 0:
        raise ValueError("Magnification cannot be zero.")
    return microscope_size / magnification
