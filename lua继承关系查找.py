#python3
import os
import re
import codecs
import json

class_dict_json='class_dict.json'
code_file_suffix='lua'
pattern_find_class=re.compile('class\("(.*?)",?(.*)?\)');


def init_class_dict():
	class_dict=dict()
	if os.path.isfile('class_dict.json'):
		class_dict=json.load(codecs.open(class_dict_json,'r','utf8'))
	else:
		rootpath=input('输入代码根目录:	')
		for item in os.walk(rootpath):
			path=item[0]
			files=item[2]
			for filename in files:
				if filename.split('.')[-1]!=code_file_suffix:
					continue;
				with codecs.open(os.path.join(path,filename),'r','utf8') as f:
					for line in f:
						pattern_result=pattern_find_class.findall(line)
						if pattern_result!=[]:
							class_dict[pattern_result[0][0].strip()]=pattern_result[0][1].strip()
							break;
		json.dump(class_dict,codecs.open(class_dict_json,'w','utf8'))
	return class_dict

def find_class(classname,class_dict):
	classname=classname.strip()
	print(classname);
	while class_dict.get(classname,None):
		classname=class_dict.get(classname,None);
		print(classname);

if __name__=='__main__':
	class_dict=init_class_dict()
	classname=input('输入要查询的类:  ')
	find_class(classname,class_dict);
