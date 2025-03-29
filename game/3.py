with open("config.txt", "r") as f:
    config = f.readlines()
    config_dict = {}
    for line in config:
        key, value = line.strip().split("=")
        config_dict[key] = value
    icon_path = config_dict.get("icon_path", "").strip()
    bg_img_path = config_dict.get("bg_img_path", "").strip()
    player_img_path = config_dict.get("player_img_path", "").strip()
    ball_img_path = config_dict.get("ball_img_path", "").strip()
    sound_path = config_dict.get("sound_path", "").strip()
    list_config = list(config_dict.values())  # 0图标1背景2板3球4音效
    print(list_config[0])
    print(list_config[1])
    print(list_config[2])
    print(list_config[3])
    print(list_config[4])
