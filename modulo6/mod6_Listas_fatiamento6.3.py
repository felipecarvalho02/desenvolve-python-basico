{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f1166633-1182-4601-86d0-ec83702a585a",
   "metadata": {},
   "outputs": [],
   "source": [
    "nums = [19, 22, -10, 4, -2, -3, 5, 6, -17, -4, -1, 67, 98, -23, -6]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8bf394e2-a866-4b18-a2dc-cefc0443a604",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 19maior ate agora\n",
      "1 22maior ate agora\n",
      "2 -103 44 -25 -36 57 68 -179 -410 -111 67maior ate agora\n",
      "12 98maior ate agora\n",
      "13 -2314 -6\n",
      "Maior ao final do laço: 12 98\n"
     ]
    }
   ],
   "source": [
    "nums = [19, 22, -10, 4, -2, -3, 5, 6, -17, -4, -1, 67, 98, -23, -6]\n",
    "\n",
    "idx_maior, val_maior = 0, float('-inf')\n",
    "\n",
    "for i in range(len(nums)): #iterando nos valores\n",
    "    print(i, nums[i], end = '')\n",
    "    if nums[i] > val_maior:\n",
    "        val_maior = nums[i] #registrando maior valor (ate agora)\n",
    "        idx_maior = i      # registrando indice do maior valor\n",
    "        print('maior ate agora')\n",
    "\n",
    "\n",
    "\n",
    "print('\\nMaior ao final do laço:', idx_maior, val_maior)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e2209db3-2224-46c1-89b6-9ef0bfa98c61",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "inicio do laço 0 19\n",
      "inicio do laço 1 22\n",
      "inicio do laço 2 -10\n",
      "Inicio nova fatia 1\n",
      "inicio do laço 3 4\n",
      "Maior fatia ate agora 1\n",
      "inicio do laço 4 -2\n",
      "Inicio nova fatia 1\n",
      "inicio do laço 5 -3\n",
      "inicio do laço 6 5\n",
      "Maior fatia ate agora 2\n",
      "inicio do laço 7 6\n",
      "inicio do laço 8 -17\n",
      "Inicio nova fatia 1\n",
      "inicio do laço 9 -4\n",
      "inicio do laço 10 -1\n",
      "inicio do laço 11 67\n",
      "Maior fatia ate agora 3\n",
      "inicio do laço 12 98\n",
      "inicio do laço 13 -23\n",
      "Inicio nova fatia 1\n",
      "inicio do laço 14 -6\n"
     ]
    }
   ],
   "source": [
    "nums = [19, 22, -10, 4, -2, -3, 5, 6, -17, -4, -1, 67, 98, -23, -6]\n",
    "\n",
    "inicio_fatia_maior, tam_fatia_maior = 0, 0\n",
    "inicio_fatia_atual, tam_fatia_atual = 0, 0\n",
    "\n",
    "for i in range(len(nums)):\n",
    "    print('Inicio do laço', i, nums[i])\n",
    "    if nums[i] < 0:\n",
    "        tam_fatia_atual += 1\n",
    "        if tam_fatia_atual == 1:\n",
    "            print('Inicio nova fatia', tam_fatia_atual)\n",
    "            inicio_fatia_atual = i\n",
    "    else:\n",
    "        if tam_fatia_atual > tam_fatia_maior:\n",
    "            print('Maior fatia ate agora', tam_fatia_atual)\n",
    "            tam_fatia_maior = tam_fatia_atual\n",
    "            inicio_fatia_maior = inicio_fatia_atual\n",
    "        tam_fatia_atual = 0\n",
    "\n",
    "print(inicio_fatia_maior, tam_fatia_maior)\n",
    "del nums[inicio_fatia_maior:inicio_fatia_maior+tam_fatia_maior]\n",
    "print(nums)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6765a947-270c-436c-8cbb-40435d150943",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
