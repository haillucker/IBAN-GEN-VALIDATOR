#!/usr/bin/python
# -*- coding: utf-8 -*-

# ( -- IMPORTS -- ) #
from random import *
import random
import time
import requests
import string
import thread

# ( -- LOGO * INFO -- ) #
bugs = '''
   ____  ___ ____    _    _   _        ____ _____ _   _ 
  / __ \|_ _| __ )  / \  | \ | |      / ___| ____| \ | |
 / / _` || ||  _ \ / _ \ |  \| |_____| |  _|  _| |  \| |
| | (_| || || |_) / ___ \| |\  |_____| |_| | |___| |\  |
 \ \__,_|___|____/_/   \_\_| \_|      \____|_____|_| \_|
  \____/                                                
\n[$] BUGS IBAN GEN/VALIDATOR.
[$] URL = ('https://www.Brazzers.com/').
[$] SCRIPT PROGRAMMED BY BUGS WITH PYTHON2.
'''
#################################
# ( -- PROGRAMMED BY @BUGS -- ) #
#################################

# ( -- FULL SCRIPT -- ) #
print bugs
print '[X] YOU CAN CHOOSE [GERMANY[DE]/FRANCE[FR]/SPAIN[ES]/ITALIA[IT]].'
print ''
# -------------------------------- ## -------------------------------- #
iban_co = raw_input('[X] ENTER YOUR IBAN COUNTRY NAME OR CODE X> ')
# -------------------------------- ## -------------------------------- #
if str(iban_co) == 'DE' or str(iban_co) == 'GERMANY':
	# //DE IBAN
	def de_chk(a, ab):
		de_iban = 'DE'+str(random.randint(00,99))+'50010517'+str(random.randint(0000000000,9999999999))
		chk_req = requests.post('https://check-iban.com/proxy.php?iban='+de_iban)
		if 'Diese IBAN ist nicht korrekt.' in chk_req.content:
			print '[X] INVALID GERMANY IBAN [ '+de_iban+' ].'
			pass
		elif 'Diese IBAN ist formal korrekt.' in chk_req.content:
			print '[X] VALID GERMANY IBAN [ '+de_iban+' ].'
			with open('VALID_DE.txt','a+') as f:
				f.write('[X] VALID GERMANY IBAN [ '+de_iban+' ].')
				f.close()
		else:
			print '[X] UNKNOWN GERMANY IBAN [ '+de_iban+' ].'
	while 1:
		thread.start_new_thread(de_chk, ('BUGS', 10))
		time.sleep(0.25)
	# -------------------------------- ## -------------------------------- ## -------------------------------- #
elif str(iban_co) == 'FR' or str(iban_co) == 'FRANCE':
	# //FR IBAN
	def fr_chk(a, ab):
		fr_iban = 'FR'+str(random.randint(00,99))+'30066'+str(random.randint(000000000000000000,999999999999999999))
		chk_req = requests.post('https://check-iban.com/proxy.php?iban='+fr_iban)
		if 'This is a valid IBAN.' in chk_req.content:
			print '[X] INVALID FRANCE IBAN [ '+fr_iban+' ].'
			pass
		else:
			print '[X] VALID FRANCE IBAN [ '+fr_iban+' ].'
			with open('VALID_FR.txt','a+') as f:
				f.write('[X] VALID FRANCE IBAN [ '+fr_iban+' ].')
				f.close()
	while 1:
		thread.start_new_thread(fr_chk, ('BUGS', 10))
		time.sleep(0.25)
	# -------------------------------- ## -------------------------------- ## -------------------------------- #
elif str(iban_co) == 'ES' or str(iban_co) == 'SPAIN':
	# //ES IBAN
	def es_chk(a, ab):
		es_iban = 'ES'+str(random.randint(0000000000000000000000,9999999999999999999999))
		chk_req = requests.post('https://check-iban.com/proxy.php?iban='+es_iban)
		if 'This is a valid IBAN.' in chk_req.content:
			print '[X] VALID SPAIN IBAN [ '+es_iban+' ].'
			with open('VALID_ES.txt','a+') as f:
				f.write('[X] VALID SPAIN IBAN [ '+es_iban+' ].')
				f.close()
		else:
			print '[X] INVALID SPAIN IBAN [ '+es_iban+' ].'
			pass
	while 1:
		thread.start_new_thread(es_chk, ('BUGS', 10))
		time.sleep(0.25)
	# -------------------------------- ## -------------------------------- ## -------------------------------- #
elif str(iban_co) == 'IT' or str(iban_co) == 'ITALY':
	# //IT IBAN
	def it_chk(a, ab):
		it_iban = 'IT'+str(random.randint(00,99))+''.join(random.choice(string.ascii_uppercase) for _ in range(1))+'0300203280'+str(random.randint(000000000000,999999999999))
		chk_req = requests.post('https://check-iban.com/proxy.php?iban='+it_iban)
		if 'This is a valid IBAN.' in chk_req.content:
			print '[X] VALID ITALY IBAN [ '+it_iban+' ].'
			with open('VALID_IT.txt','a+') as f:
				f.write('[X] VALID ITALY IBAN [ '+it_iban+' ].')
				f.close()
		else:
			print '[X] INVALID ITALY IBAN [ '+it_iban+' ].'
			pass
	while 1:
		thread.start_new_thread(it_chk, ('BUGS', 10))
		time.sleep(0.25)
	# -------------------------------- ## -------------------------------- ## -------------------------------- #
else:
	# //OUT PUT
	print '[X] PLEASE CHOOSE CORRECT COUNTRY NAME OR CODE.'
	# -------------------------------- ## -------------------------------- ## -------------------------------- #

# // ------------------------------ \\ #
     # //DE{21}50010517{7325642159}
   # //FR{33}30066{211244248463881845}
     # //ES{0320803667113276654123}
   # //IT{18A}0300203280{974228927459}
# // ------------------------------ \\ #