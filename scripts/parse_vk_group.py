from sys import argv
import json

import vk_api

from config import vk_login, vk_password


def auth():
    vk_session = vk_api.VkApi(vk_login, vk_password)
    vk_session.auth()
    return vk_session


def get_posts(group_id, out_file):
    vk_session = auth()
    tools = vk_api.VkTools(vk_session)
    cnt_total = 0

    with open(out_file, "w") as f:
        while True:
            wall = tools.get_all("wall.get", 100, {"domain": group_id})
            f.write("\n".join(map(json.dumps, wall["items"])))    
            cnt_total += len(wall["items"])
            print("Loading {}/{}".format(cnt_total, wall["count"]))
            if cnt_total >= wall["count"]:
                break


if __name__ == "__main__":
    get_posts(argv[1], argv[2])
