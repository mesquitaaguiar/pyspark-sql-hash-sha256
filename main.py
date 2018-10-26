import sys
import hashlib
from datetime import datetime, timedelta

dias_ant = int(5)

reload(sys)
sys.setdefaultencoding('utf8')

def encrypt_string(hash_string):
	return hashlib.sha256(hash_string.encode()).hexdigest()

def s_string(var_string,crypt_string):
	if var_string is None or var_string == 'None' :
		return ""
	elif crypt_string :
		return encrypt_string(var_string)
	else :
		return var_string


sql = " SELECT nf,cfop,cpf "
sql = sql + " FROM <db>.<table_nf> WHERE dt = " + (datetime.now() - timedelta(days=dias_ant)).strftime('%Y%m%d');
_recordsetA = sqlContext.sql(sql)

sql = " SELECT nf as nfa,produto "
sql = sql + " FROM <db>.<table_produto> WHERE dt = " + (datetime.now() - timedelta(days=dias_ant)).strftime('%Y%m%d');
_recordsetZ = sqlContext.sql(sql)

if _recordsetA.count() > 0 and (_recordsetZ.count() > 0 or _INICIAL):
	_sql = _recordsetA.join(_recordsetZ,_recordsetZ.nf == _recordsetA.nfa,'left_outer')
	
	recordset = _sql.select("nf","cfop","cpf","produto").collect()
	
	print("Imprimindo...")
	
	print(str(len(recordset)) +" registro(s)")
	i = 0;
	for linha in recordset:
		print (str(i) +" "+ s_string(str(linha.nf),True) +" "+ s_string(str(linha.cfop),False) +" -- "+ s_string(str(linha.cpf),True) +" "+ s_string(str(linha.produto),False))
		i = i + 1
	
	print("Finalizando.")
else:
	print("Não pode extrair dados")

quit()
