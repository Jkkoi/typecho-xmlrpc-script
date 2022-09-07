import argparse
import xmlrpc.client
import os

ApiUrl = ""
UserName = ""
PassWD = ""

parser = argparse.ArgumentParser(description='Typecho XmlRpc 发布脚本')
parser.add_argument('--currentPath', '-f', help='文件绝对路径', required=True)
parser.add_argument('--title', '-t', help='文章标题,留空取文件名')
args = parser.parse_args()

if args.title is None:
    dir_name, full_file_name = os.path.split(args.currentPath)
    file_name, file_ext = os.path.splitext(full_file_name)
    args.title = file_name

content = {"post_type": "post", "title": args.title, "description": "", "mt_text_more": "",
           "categories": ["默认分类"]}

with open(args.currentPath, "r", encoding="utf-8") as file:
    lines = file.readlines()
    content["description"] = "".join(lines[:3:])
    content["mt_text_more"] = "".join(lines[3::])

Typecho_Server = xmlrpc.client.ServerProxy(ApiUrl)

rtn = Typecho_Server.metaWeblog.newPost(1, UserName, PassWD,
                                        content,
                                        True)
print(f"cid: {rtn}")
