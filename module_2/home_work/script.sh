pylint decrypt.py
pylint_res=$?
if [[ pylint_res -eq 0 ]];
then
  echo "Pylint OK"
else
  echo "Pylint not OK"
fi

python -m unittest tests.test_decrypt

if [[ $? -eq 0 ]] && [[ pylint_res -eq 0 ]];
then
    echo "всё OK"
else
    echo "Имеются ошибки"
fi
