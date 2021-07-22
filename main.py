import tkinter


class ConvertToMetric:
    def __init__(self):
        pass

    @staticmethod
    def to_kilometers(**kwargs):
        if kwargs.get("miles"):
            return kwargs.get("miles") * 1.609344
        else:
            return False


converter = ConvertToMetric()

# Setup Window
window = tkinter.Tk()
window.title("Miles to Kilometers")
window.minsize(400, 300)

# Initialize widgets
mileage_entry = tkinter.Entry()
convert_button = tkinter.Button()
km_label = tkinter.Label()


def button_handler():
    # Get data and submit to conversion class.
    miles_entered = int(mileage_entry.get())
    converted_value = converter.to_kilometers(miles=miles_entered)
    km_label["text"] = f"Kilometers: {converted_value}"


# Configure widgets
convert_button["text"] = "Convert"
convert_button["command"] = button_handler
km_label["text"] = "Kilometers: "

# Pack widgets
mileage_entry.pack()
convert_button.pack()
km_label.pack()

# Run app
window.mainloop()
