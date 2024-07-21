{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "dc53bfd6-f6dc-416a-b8c0-e678fc3692c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "請輸入密碼 321\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "密碼錯誤還可輸入2次\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "請輸入密碼 123\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "密碼正確\n"
     ]
    }
   ],
   "source": [
    "password = '123'\n",
    "pos = 3\n",
    "####################################\n",
    "chk = ''\n",
    "while chk !='ok':\n",
    "    if pos > 0 :\n",
    "        ans = input ('請輸入密碼')\n",
    "        if ans == password:\n",
    "            chk = 'ok'\n",
    "            print('密碼正確')\n",
    "        else:\n",
    "            pos -= 1\n",
    "            print ('密碼錯誤還可輸入'+ str(pos) +'次')\n",
    "    else :\n",
    "        print('密碼輸入超過3次')\n",
    "        break\n",
    "if chk != 'ok':\n",
    "    print('請重新執行')\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9acd11ee-fa46-4d55-aa95-ef4f7ec4ef62",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
