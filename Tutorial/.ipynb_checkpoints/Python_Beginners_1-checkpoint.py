{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "7b3d38bf",
   "metadata": {},
   "source": [
    "# ROUND"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "17b3cfb4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "print(round(4.55))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "3c567548",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.522\n"
     ]
    }
   ],
   "source": [
    "print(round(4.5225,3))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3da9702a",
   "metadata": {},
   "source": [
    "# DIVMOD - It returns the quocient and the reminder (// or % can also be used)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "49bdaa14",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(5, 2)\n"
     ]
    }
   ],
   "source": [
    "print(divmod(27,5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "17ea9fc6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "G=divmod(27,5)\n",
    "\n",
    "print (G[0])\n",
    "\n",
    "print(G[1])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e262f32b",
   "metadata": {},
   "source": [
    "# IsInstabce - returns true if the foirst argument is an instance of a class"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b5b76c8a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "print(isinstance(1, float))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "f2e6ff5f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print(isinstance(1, int))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "281ff5ff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print(isinstance (1, (int, float, bool)))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7b40be6e",
   "metadata": {},
   "source": [
    "# Power - pow(3,3,9) = (3**3)/9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "399f3e36",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "27"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pow(3,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "6e344b22",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "27"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "3**3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "e4f83ce6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pow(3,3,9)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "11a833d4",
   "metadata": {},
   "source": [
    "# Taking input from the user"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "3f78ba55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Type a number:4\n",
      "Type another number:7\n",
      "The addition of 4 and 7 is: 11 \n"
     ]
    }
   ],
   "source": [
    "num1 = int(input(\"Type a number:\"))\n",
    "num2 = int(input(\"Type another number:\"))\n",
    "sum = num1+num2\n",
    "print(\"The addition of {} and {} is: {} \".format(num1, num2, sum))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9f9f4511",
   "metadata": {},
   "source": [
    "# Control Flow, Conditional Statemen"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "da270c6c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Type a number:4\n",
      "Type another number:4\n",
      " 4 is same as 4 \n",
      ">19\n"
     ]
    }
   ],
   "source": [
    "num1 = int(input(\"Type a number:\"))\n",
    "num2 = int(input(\"Type another number:\"))\n",
    "\n",
    "if num1 > num2:\n",
    "    print(\" {} is greater than {} \" .format(num1, num2))\n",
    "elif num1 < num2:\n",
    "    print(\" {} is less than {} \" .format(num1, num2))\n",
    "else:\n",
    "    print (\" {} is same as {} \" .format(num1, num2))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bb254e14",
   "metadata": {},
   "source": [
    "# Comments"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "180fe665",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Single line comment\n",
    "\n",
    "\"\"\"\"\n",
    "Double line comment\n",
    "Double line comment\n",
    "\"\"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6e6a0b7d",
   "metadata": {},
   "source": [
    "# While loops"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "ce499e7b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Type a number5\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "done\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"Type a number\"))\n",
    "i = 1\n",
    "while i<=n:\n",
    "    print(i)\n",
    "    i=i+1\n",
    "print (\"done\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "defb2309",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "intDiv = 10//3\n",
    "\n",
    "print(intDiv)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "52209aec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Variable   Type    Data/Info\n",
      "----------------------------\n",
      "b          str     str\n",
      "cv         str     strdtr\n",
      "intDiv     int     3\n",
      "numm       str     dtr\n"
     ]
    }
   ],
   "source": [
    "%whos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "fab257e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n",
      "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]\n"
     ]
    }
   ],
   "source": [
    " L = []\n",
    " for i in range (10):\n",
    "    print(i+1)\n",
    "    L.append(i**2)\n",
    "print (L)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "822bf3be",
   "metadata": {},
   "source": [
    "# Print Grade"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "b30a7cab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the grade: 50\n",
      " 50: Grade = C\n"
     ]
    }
   ],
   "source": [
    "score = int(input('Enter the grade: '))\n",
    "if score >= 70:\n",
    "    print(\" {}: Grade = A\" .format(score))\n",
    "    \n",
    "elif score <= 69 and score>= 60:\n",
    "    print(\" {}: Grade = B\" .format(score))\n",
    "    \n",
    "elif score <= 59 and score>= 50:\n",
    "    print(\" {}: Grade = C\" .format(score))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "5b7e1b71",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input a number: 10\n",
      "1\n",
      "3\n",
      "5\n",
      "7\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"Input a number: \"))\n",
    "i = 1\n",
    "if n > 0:\n",
    "    while i < n:\n",
    "        if i%2 != 0:\n",
    "            print (i)\n",
    "        else:\n",
    "            pass\n",
    "        i = i+1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "db136ae1",
   "metadata": {},
   "source": [
    "# For Loop \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "154f91e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "n = 10\n",
    "i = 1\n",
    "while True:\n",
    "    if i%n == 0:\n",
    "        \n",
    "        break\n",
    "    else:\n",
    "        i = i+1\n",
    "        continue\n",
    "print (\"Done\")       "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "43f80c76",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "628c66dd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "66890814",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27fb6d78",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d82428dd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6eb1e159",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38b8892c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "862f4db7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "39f595cd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a48ce4e5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "03a9ef84",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc922033",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e977eaa2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b7868925",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "063743e5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f20c18ac",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "93438fcd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8143993d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ba84a2d2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9d9ed96b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1cb4330",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b8ce0ae9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8bccc3cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53df22ca",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "761f358f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a197df67",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b3a4e68",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "07a1a257",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e02e091",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7fcab60",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "992a3dd7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "86e0fbeb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b705094",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eadab3be",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "eca29a42",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6957b0b5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "89c6dbc6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a2339c0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e4407331",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18277ab9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "769b464f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d7497076",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aadb618a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "49ac5f06",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e927d2a9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3c4baa4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c05de29e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d3f8b60c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78f98d5d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d2ffcf05",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b2fd4db6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c75fc1d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7da3b395",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0b9feee4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ce1673d",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "14c8e2db",
   "metadata": {},
   "source": [
    "# First Code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "435bf40d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello World\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ef93677",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9af632ab",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "02f13206",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n",
      "The smallest number in the list is -5\n"
     ]
    }
   ],
   "source": [
    "#search minFromList(L,n)\n",
    "\n",
    "L = [10, 30,-5,9,-1,13]\n",
    "print(L)\n",
    "print(\"The smallest number in the list is\", L[0])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "2f9522dd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "8\n",
      "4.894\n"
     ]
    }
   ],
   "source": [
    "print (round(4.338))\n",
    "print (round(7.838))\n",
    "print (round(4.894, 3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "615ffb85",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(5, 2)\n",
      "(3, 0)\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "#27/5 = 5 rem 2\n",
    "\n",
    "print (divmod(27, 5))\n",
    "print (divmod(9, 3))\n",
    "\n",
    "div = (divmod(19, 3))\n",
    "print (div[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "6bce4a1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3 4\n"
     ]
    }
   ],
   "source": [
    "a =10//3\n",
    "b =12//3\n",
    "print (a, b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "d106c0b6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False False\n"
     ]
    }
   ],
   "source": [
    "res = isinstance(2, float)\n",
    "ress = isinstance(2+3j, (int, complex))\n",
    "print (res, ress)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b58df97",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pow(2,2)\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "d35fe771",
   "metadata": {},
   "source": [
    "#Taking user input"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "6ea784d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "qc\n"
     ]
    }
   ],
   "source": [
    "strg = input(\"Enter your name: \")\n",
    "print (strg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "dceb9a60",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ogun\n"
     ]
    }
   ],
   "source": [
    "print (str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "3b1c7e37",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "200\n"
     ]
    }
   ],
   "source": [
    "intNum = int(input (\"Enter a real number: \"))\n",
    "print (intNum*2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "8049677e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You entered a real number: 100.\n"
     ]
    }
   ],
   "source": [
    "#isinstance(intNum, int)\n",
    "\n",
    "if (type (intNum) == int): \n",
    "    print (\"You entered a real number: {}.\".format(intNum))\n",
    "else:\n",
    "    print (\"You did not enter a real number {}.\". format(intNum))\n",
    "  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "5e0d6092",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'Bukunmi', 'age': 15}\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "#Dictionary \n",
    "dic = {\"name\":\"Bukunmi\", \"age\":15}\n",
    "print (dic)\n",
    "print (\"age\" in dic)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "507c6b40",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 3, 'ëst', [2, 3], 'you']\n",
      "[1, 3, 'ëst', [2, 3], 'you', 8]\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "#list\n",
    "lst = [1, 3, \"ëst\", [2, 3], \"you\"]\n",
    "print (lst) \n",
    "lst.append(8)\n",
    "print (lst) \n",
    "lst[0] = 5\n",
    "print (len(lst)) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "8b10f06a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 3, 'you')\n"
     ]
    }
   ],
   "source": [
    "#Tuple\n",
    "tpl = (1, 2, 3, \"you\")\n",
    "print (tpl)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "04b40287",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x is not y\n"
     ]
    }
   ],
   "source": [
    "x=0\n",
    "y=\"you\"\n",
    "\n",
    "if x==y:\n",
    "    print (\"x and y are equal\")\n",
    "else:\n",
    "    print(\"x is not y\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "a9a8c488",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 1\n",
      "2 2\n",
      "3 3\n",
      "4 4\n",
      "5 5\n",
      "6 6\n",
      "7 7\n",
      "8 8\n",
      "9 9\n",
      "10 10\n"
     ]
    }
   ],
   "source": [
    "x=0\n",
    "z = 1\n",
    "y= int(input(\"Enter your counter: \"))\n",
    "\n",
    "if(y>x):\n",
    "    while (z <= y):\n",
    "        print (z,z)\n",
    "        z+=1\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "da4dfd8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "computer\n",
      "book\n",
      "mouse\n",
      "others\n"
     ]
    }
   ],
   "source": [
    "# Loop\n",
    "\n",
    "lst = [\"computer\", \"book\", \"mouse\", \"others\"]\n",
    "\n",
    "for i in range(len (lst)):\n",
    "    print(lst[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "5ae8b152",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "#for loop with Continue\n",
    "\n",
    "for i in range (1, 10):\n",
    "    \n",
    "    if (i==5):\n",
    "        #a = 5\n",
    "        continue\n",
    "    print (i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "df63dd6a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\'os.rename (current_file_name, new_file_name)\\nos.remove (\"current_file_name\")\\n\\n#Modes \\n\\nr    Read only\\nrb   Read in binary format\\nr+   Read and wrie\\nrb+  Read and write in binary format\\nw    Write only, create if not exist\\nwb   Write only in binary, creates if not exist\\na    Append\\nab   Append in binary\\na+   Append and read\\nab+  Append and read in  binary \\nw+   Writing and reading\\nwb+Writing and reading in binary form'"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# FIle FUnctions\n",
    "\n",
    "#opens a file\n",
    "file_Object = open(file_name, [access_mode])\n",
    "\n",
    "#Renames a file\n",
    "os.rename (current_file_name, new_file_name)\n",
    "os.remove (\"current_file_name\")\n",
    "\n",
    "#Modes \n",
    "\n",
    "r    Read only\n",
    "rb   Read in binary format\n",
    "r+   Read and write\n",
    "rb+  Read and write in binary format\n",
    "w    Write only, create if not exist\n",
    "wb   Write only in binary, creates if not exist\n",
    "a    Append\n",
    "ab   Append in binary\n",
    "a+   Append and read\n",
    "ab+  Append and read in  binary \n",
    "w+   Writing and reading\n",
    "wb+Writing and reading in binary form"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No, 'expensive' is NOT present.\n"
     ]
    }
   ],
   "source": [
    "txt = \"The best things in life are free!\"\n",
    "if \"expensive\" not in txt:\n",
    "  print(\"No, 'expensive' is NOT present.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "c3a5dca9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " Hello you, welcome to Python:\n",
      " Hello you, welcome to Python:\n",
      " Hello you, welcome to Python:\n",
      " Hello you, welcome to Python:\n",
      " Hello you, welcome to Python:\n",
      " Hello you, welcome to Python:\n",
      " Hello you, welcome to Python:\n",
      " Hello you, welcome to Python:\n",
      " Hello you, welcome to Python: sir/ma, welcome to Python:\n",
      " Hello Everyone, welcome to Python:\n",
      " Hello Everyone, welcome to Python:\n",
      " Hello Everyone, welcome to Python:\n",
      " Hello Everyone, welcome to Python:\n",
      " Hello Everyone, welcome to Python:\n",
      " Hello Everyone, welcome to Python:\n",
      " Hello Everyone, welcome to Python:\n",
      " Hello Everyone, welcome to Python:\n",
      " Hello Everyone, welcome to Python:\n"
     ]
    }
   ],
   "source": [
    "#Create text Doc Write and Print\n",
    "\n",
    "import os\n",
    "#Myfiletest = \"\"\n",
    "Myfiletest = open(\"PyFileWite.txt\", \"w+\")\n",
    "\n",
    "for i in range(1, 10):\n",
    "    Myfiletest.write(\"\\n Hello you, welcome to Python:\")\n",
    "    \n",
    "Myfiletest = open(\"PyFileWite.txt\", \"r\")   \n",
    "print (Myfiletest.read())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "id": "db4f2cc3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " Hello, welcome to Python:\n",
      " Hello, welcome to Python:\n",
      " Hello, welcome to Python:\n",
      " Hello, welcome to Python:\n",
      " Hello, welcome to Python:\n",
      " Hello, welcome to Python:\n",
      " Hello, welcome to Python:\n",
      " Hello, welcome to Python:\n",
      " Hello, welcome to Python:\n"
     ]
    }
   ],
   "source": [
    "f = open(\"myfile.txt\", \"r+\")\n",
    "#f=\"\"\n",
    "for i in range(1, 10):\n",
    "    f.write(\"\\n Hello, welcome to Python:\")\n",
    "    \n",
    "f = open(\"myfile.txt\", \"r\")\n",
    "print(f.read())\n",
    "\n",
    "#=============================\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8fbe015b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "F I L E   C O N T E N T\n",
      "\n",
      " Hello you, welcome to Python:\n",
      " Hello you, welcome to Python:\n",
      " Hello you, welcome to Python:\n",
      " Hello you, welcome to Python:\n",
      " Hello you, welcome to Python:\n",
      " Hello you, welcome to Python:\n",
      " Hello you, welcome to Python:\n",
      " Hello you, welcome to Python:\n",
      " Hello you, welcome to Python: sir/ma, welcome to Python:\n",
      " Hello Everyone, welcome to Python:\n",
      " Hello Everyone, welcome to Python:\n",
      " Hello Everyone, welcome to Python:\n",
      " Hello Everyone, welcome to Python:\n",
      " Hello Everyone, welcome to Python:\n",
      " Hello Everyone, welcome to Python:\n",
      " Hello Everyone, welcome to Python:\n",
      " Hello Everyone, welcome to Python:\n",
      " Hello Everyone, welcome to Python:\n",
      "---------------------------------------------------------------------\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'os' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 14\u001b[0m\n\u001b[0;32m     12\u001b[0m     \u001b[39mprint\u001b[39m(\u001b[39m\"\u001b[39m\u001b[39m---------------------------------------------------------------------\u001b[39m\u001b[39m\"\u001b[39m)\n\u001b[0;32m     13\u001b[0m     f\u001b[39m.\u001b[39mclose()\n\u001b[1;32m---> 14\u001b[0m     os\u001b[39m.\u001b[39mremove(\u001b[39m\"\u001b[39m\u001b[39mPyFileWite.txt\u001b[39m\u001b[39m\"\u001b[39m)\n\u001b[0;32m     15\u001b[0m     \u001b[39mprint\u001b[39m(\u001b[39m\"\u001b[39m\u001b[39mFile deleted succesfully\u001b[39m\u001b[39m\"\u001b[39m)\n\u001b[0;32m     16\u001b[0m \u001b[39mexcept\u001b[39;00m \u001b[39mValueError\u001b[39;00m:\n",
      "\u001b[1;31mNameError\u001b[0m: name 'os' is not defined"
     ]
    }
   ],
   "source": [
    "#Delete Fie in Python\n",
    "\n",
    "''''from pathlib import Path\n",
    "if os.path.isfile(myfile):\n",
    "    os.remove (\"myfile\")'''\n",
    "try:\n",
    "    e  = \"An Error Occured\"\n",
    "    filepath=\"PyFileWite.txt\"\n",
    "    f = open(filepath, \"r\")\n",
    "    print(\"F I L E   C O N T E N T\")\n",
    "    print(f.read())\n",
    "    print(\"---------------------------------------------------------------------\")\n",
    "    f.close()\n",
    "    os.remove(\"PyFileWite.txt\")\n",
    "    print(\"File deleted succesfully\")\n",
    "except ValueError:\n",
    "    raise ValueError(\"An Error Occured\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "68ae2971",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "c:\\Users\\studio\\Documents\\Python Code 2022\n"
     ]
    }
   ],
   "source": [
    "from pathlib import Path\n",
    "print(Path.cwd())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3d713fe4",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'os' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m os\u001b[39m.\u001b[39mrename(\u001b[39m\"\u001b[39m\u001b[39mmyfile.txt\u001b[39m\u001b[39m\"\u001b[39m,  \u001b[39m\"\u001b[39m\u001b[39mnew_file_name\u001b[39m\u001b[39m\"\u001b[39m)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'os' is not defined"
     ]
    }
   ],
   "source": [
    "os.rename(\"myfile.txt\",  \"new_file_name\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "09960970",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "82569\n"
     ]
    }
   ],
   "source": [
    "exp = [200, 3480, 5439, 8744, 7839, 56867]\n",
    "\n",
    "total = 0\n",
    "\n",
    "for i in exp:\n",
    "    total = total+i\n",
    "    i+=1\n",
    "print(total)\n"
   ]
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
