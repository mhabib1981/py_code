import re
import os

sourcefile='/root/test_data.txt' 
targetfile=file(((sourcefile.split('/')[-1]).split('.')[0]) + "_URLs", 'w')

if os.path.exists(sourcefile):
	raw_data=open(sourcefile, 'r').readlines();
	for line in raw_data:
		if "HTTP URI" in line:
			ip_pattern=re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
			src_ip=re.findall(ip_pattern, line)
			xl=re.sub(r'^(.*)HTTP URI == ',"",line);
	                xr=re.sub(r';(.*)',"",xl);
			if "n/a" not in xr:
				refined_data="http://" + src_ip[0] + xr;
				print refined_data
				targetfile.write(refined_data)
