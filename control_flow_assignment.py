{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "53163d85",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "----- Task 1: Discount Calculation -----\n",
      "Enter order amount: 100\n",
      "Discount applied: 0 %\n",
      "Final amount: 100.0\n"
     ]
    }
   ],
   "source": [
    "# Task 1: Discount Rules (if / elif / else)\n",
    "print(\"----- Task 1: Discount Calculation -----\")\n",
    "\n",
    "order_input = input(\"Enter order amount: \")\n",
    "\n",
    "# Handle non-numeric input\n",
    "if not order_input.replace('.', '', 1).isdigit():\n",
    "    print(\"Error: Please enter a valid numeric value.\")\n",
    "else:\n",
    "    order_amount = float(order_input)\n",
    "\n",
    "    if order_amount >= 2000:\n",
    "        discount = 0.15\n",
    "    elif order_amount >= 1500:\n",
    "        discount = 0.10\n",
    "    elif order_amount >= 1000:\n",
    "        discount = 0.07\n",
    "    else:\n",
    "        discount = 0\n",
    "\n",
    "    discount_amount = order_amount * discount\n",
    "    final_amount = order_amount - discount_amount\n",
    "\n",
    "    print(\"Discount applied:\", discount * 100, \"%\")\n",
    "    print(\"Final amount:\", final_amount)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8c73a5dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "----- Task 2: Multiple Orders -----\n",
      "Order: 1200 Discount: 7.000000000000001 % Final: 1116.0\n",
      "Order: 2500 Discount: 15.0 % Final: 2125.0\n",
      "Order: 800 Discount: 0 % Final: 800\n",
      "Order: 1750 Discount: 10.0 % Final: 1575.0\n",
      "Order: 3000 Discount: 15.0 % Final: 2550.0\n",
      "Total revenue after discount: 8166.0\n",
      "Number of discounted orders: 4\n"
     ]
    }
   ],
   "source": [
    "# Task 2: Process Multiple Orders (for loop)\n",
    "print(\"\\n----- Task 2: Multiple Orders -----\")\n",
    "\n",
    "orders = [1200, 2500, 800, 1750, 3000]\n",
    "total_revenue = 0\n",
    "discounted_orders = 0\n",
    "\n",
    "for order in orders:\n",
    "\n",
    "    if order >= 2000:\n",
    "        discount = 0.15\n",
    "    elif order >= 1500:\n",
    "        discount = 0.10\n",
    "    elif order >= 1000:\n",
    "        discount = 0.07\n",
    "    else:\n",
    "        discount = 0\n",
    "\n",
    "    discount_amount = order * discount\n",
    "    final_amount = order - discount_amount\n",
    "\n",
    "    if discount > 0:\n",
    "        discounted_orders += 1\n",
    "\n",
    "    total_revenue += final_amount\n",
    "\n",
    "    print(\"Order:\", order,\n",
    "          \"Discount:\", discount * 100, \"%\",\n",
    "          \"Final:\", final_amount)\n",
    "\n",
    "print(\"Total revenue after discount:\", total_revenue)\n",
    "print(\"Number of discounted orders:\", discounted_orders)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0750b134",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "----- Task 3: User Menu -----\n",
      "\n",
      "1 - Add order\n",
      "2 - Show orders and total\n",
      "q - Quit\n",
      "Enter choice: 1\n",
      "Enter order amount: 2\n",
      "Order added.\n",
      "\n",
      "1 - Add order\n",
      "2 - Show orders and total\n",
      "q - Quit\n",
      "Enter choice: q\n",
      "Exiting menu.\n"
     ]
    }
   ],
   "source": [
    "# Task 3: User Menu (while loop + break/continue)\n",
    "# ==========================================\n",
    "\n",
    "print(\"\\n----- Task 3: User Menu -----\")\n",
    "\n",
    "order_list = []\n",
    "\n",
    "while True:\n",
    "\n",
    "    print(\"\\n1 - Add order\")\n",
    "    print(\"2 - Show orders and total\")\n",
    "    print(\"q - Quit\")\n",
    "\n",
    "    choice = input(\"Enter choice: \")\n",
    "\n",
    "    if choice == \"1\":\n",
    "        amount = input(\"Enter order amount: \")\n",
    "\n",
    "        if not amount.replace('.', '', 1).isdigit():\n",
    "            print(\"Invalid input. Try again.\")\n",
    "            continue\n",
    "\n",
    "        order_list.append(float(amount))\n",
    "        print(\"Order added.\")\n",
    "\n",
    "    elif choice == \"2\":\n",
    "        total = 0\n",
    "\n",
    "        for order in order_list:\n",
    "            if order >= 2000:\n",
    "                discount = 0.15\n",
    "            elif order >= 1500:\n",
    "                discount = 0.10\n",
    "            elif order >= 1000:\n",
    "                discount = 0.07\n",
    "            else:\n",
    "                discount = 0\n",
    "\n",
    "            total += order - (order * discount)\n",
    "\n",
    "        print(\"Orders:\", order_list)\n",
    "        print(\"Total after discount:\", total)\n",
    "\n",
    "    elif choice == \"q\":\n",
    "        print(\"Exiting menu.\")\n",
    "        break\n",
    "\n",
    "    else:\n",
    "        print(\"Invalid option.\")\n",
    "        continue\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "27159576",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "----- Task 5: Daily Sales Processing -----\n",
      "Running total: 200\n",
      "Running total: 350\n",
      "No sales today.\n",
      "Running total: 750\n",
      "Running total: 1250\n",
      "Corrupted data found. Stopping.\n",
      "Final total sales: 1250\n"
     ]
    }
   ],
   "source": [
    "# Task 5: Loop Control with break & continue\n",
    "# ==========================================\n",
    "\n",
    "print(\"\\n----- Task 5: Daily Sales Processing -----\")\n",
    "\n",
    "sales = [200, 150, 0, 400, 500, -1, 300]\n",
    "total_sales = 0\n",
    "\n",
    "for day in sales:\n",
    "\n",
    "    if day == -1:\n",
    "        print(\"Corrupted data found. Stopping.\")\n",
    "        break\n",
    "\n",
    "    if day == 0:\n",
    "        print(\"No sales today.\")\n",
    "        continue\n",
    "\n",
    "    total_sales += day\n",
    "    print(\"Running total:\", total_sales)\n",
    "\n",
    "print(\"Final total sales:\", total_sales)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ca06ca8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
