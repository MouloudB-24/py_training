def add_setting(settings_dict: dict, settings_tuple: tuple) -> str:
	key = settings_tuple[0].lower()
	value = settings_tuple[1].lower()
	
	if key in settings_dict:
		return f"Setting '{key}' already exists! Cannot add a new setting with this name."
	
	settings_dict[key] = value
	return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings_dict: dict, settings_tuple: tuple) -> str:
	key = settings_tuple[0].lower()
	value = settings_tuple[1].lower()
	
	if key in settings_dict:
		settings_dict[key] = value
		return f"Setting '{key}' updated to '{value}' successfully!"
	return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings_dict: dict, key: str) -> str:
	key = key.lower()

	if key in settings_dict:
		del settings_dict[key]
		return f"Setting '{key}' deleted successfully!"
	return f"Setting not found!"


def view_settings(settings_dict: dict) -> str:
	if not settings_dict:
		return f"No settings available."

	message = "Current User Settings:"
	for key, value in settings_dict.items():
		message += f"\n{key.capitalize()}: {value}"
	return message


test_settings = {'theme': 'light'}

if __name__ == "__main__":
	settings_dict = {}
	add_setting(settings_dict, ("theme", "dark"))
	add_setting(settings_dict, ("language", "english"))
	print(view_settings(settings_dict))

