{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ubdll/Python-self-service-cashier/blob/main/Project_Python.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 595,
      "metadata": {
        "id": "q0SVaHdgGgco"
      },
      "outputs": [],
      "source": [
        "from prettytable import PrettyTable\n",
        "class Transaction:\n",
        "    def __init__(self):\n",
        "        self.items = []\n",
        "\n",
        "    def add_item(self, name, quantity, price):\n",
        "      '''fungsi untuk menambahkan item pada transaksi'''\n",
        "      if type(quantity)!=int: \n",
        "        print(\"Quantity harus berbentuk angka\") #validasi quantity harus berbentuk int\n",
        "      elif type(price)!=int:\n",
        "        print(\"Harga harus berbentuk angka\") #validasi harga harus berbentuk int\n",
        "      else:\n",
        "        self.items.append({'name': name, 'quantity': quantity, 'price': price})\n",
        "        print(\"Barang yang anda beli adalah:\")\n",
        "      for item in self.items:  \n",
        "        print(item)\n",
        "        \n",
        "\n",
        "    def update_item_name(self, name, new_name):\n",
        "      '''fungsi untuk mengupdate nama item'''\n",
        "      for item in self.items:\n",
        "        if item['name'] == name:\n",
        "          item['name'] = new_name\n",
        "          #dari name ---> new_name\n",
        "          break\n",
        "      print(f\"nama dari {name} berubah menjadi {new_name}\" )\n",
        "              \n",
        "    def update_item_qty(self, name, new_qty):\n",
        "      '''fungsi untuk update quantity'''\n",
        "      for item in self.items:\n",
        "        if item['name'] == name:\n",
        "          item['quantity'] = new_qty\n",
        "      #dari quantity yg tertera dari name, dijadikan new_qty\n",
        "          break\n",
        "      print(f\"Quantity {name} berubah menjadi {new_qty}\")\n",
        "    \n",
        "    def update_item_price(self, name, new_price):\n",
        "      '''fungsi untuk update harga barang'''\n",
        "      for item in self.items:\n",
        "        if item['name'] == name:\n",
        "          item['price'] = new_price\n",
        "            #dari harga yg tertera dari name, dijadikan new_price\n",
        "          break\n",
        "\n",
        "    def delete_item(self, name):\n",
        "      '''fungsi untuk menghapus item'''\n",
        "      for item in self.items:\n",
        "          if item['name'] == name:\n",
        "            self.items.remove(item)\n",
        "      #menghapus item yg memiliki nama yang sama dengan nama yg di input\n",
        "            break\n",
        "      print(f\"{name} berhasil di hapus!\")\n",
        "        \n",
        "      for item in self.items:\n",
        "        print(item)\n",
        "\n",
        "    def reset_transaction(self):\n",
        "        '''fungsi untuk reset transaksi'''\n",
        "        self.items = []\n",
        "        print(\"semua item berhasil dihapus!\")\n",
        "\n",
        "    def get_total(self):\n",
        "        '''fungsi untuk menghitung total'''\n",
        "        total = 0\n",
        "        for item in self.items:\n",
        "            total += item['quantity'] * item['price']\n",
        "        #Quantity di tiap item dikali price\n",
        "        return total\n",
        "\n",
        "    def check_order(self):\n",
        "        '''fungsi untuk menghitung total.'''\n",
        "        for item in self.items:\n",
        "            if not item['name'] or not item['quantity'] or not item['price']:\n",
        "                print('Terdapat kesalahan input pada pemesanan!')\n",
        "                return\n",
        "        print(f'Pemesanan sudah benar.')\n",
        "        table = PrettyTable()\n",
        "        table.field_names = ['Nama', 'Kuantitas', 'Harga']\n",
        "        for item in self.items:\n",
        "          table.add_row([item['name'], item['quantity'], item['price']])\n",
        "        #Mengeluarkan tabel utk barang yang sudah dibeli\n",
        "        print(table)\n",
        "\n",
        "    def total_price(self):\n",
        "      '''fungsi untuk menghitung total harga transaksi'''\n",
        "      total = 0\n",
        "      for item in self.items:\n",
        "            total += item['quantity'] * item['price']\n",
        "      if total > 500_000:\n",
        "        discount = (total*0.1)\n",
        "        total = (total - discount)\n",
        "        print(f\"Total belanja Rp {total} dengan diskon 10%.\")        \n",
        "\n",
        "      elif total > 300_000:\n",
        "        discount = (total * 0.08)\n",
        "        total = (total - discount)\n",
        "        print(f\"Total belanja Rp {total} dengan diskon 8%.\")\n",
        "\n",
        "      elif total > 200_000:\n",
        "        discount = (total * 0.05)\n",
        "        total = int(total - discount)\n",
        "        print(f\"Total belanja Rp {total} dengan diskon 5%.\")\n",
        "\n",
        "      else:\n",
        "        print(f\"Total belanja Anda adalah Rp {total}.\")\n",
        "      for item in self.items:\n",
        "        print(item)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 596,
      "metadata": {
        "id": "Fgk9_1zf3cIh"
      },
      "outputs": [],
      "source": [
        "trnsct_123 = Transaction()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "trnsct_123.add_item(\"cakue\",2,50000)"
      ],
      "metadata": {
        "id": "tLrAphtcDYjR",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "4d7343df-8f90-494b-8554-584973e3b191"
      },
      "execution_count": 597,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Barang yang anda beli adalah:\n",
            "{'name': 'cakue', 'quantity': 2, 'price': 50000}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "trnsct_123.add_item(\"kopi\",3,70000)"
      ],
      "metadata": {
        "id": "SviWTZ65amG8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "455631b2-d989-4b45-d124-474e907ddf57"
      },
      "execution_count": 598,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Barang yang anda beli adalah:\n",
            "{'name': 'cakue', 'quantity': 2, 'price': 50000}\n",
            "{'name': 'kopi', 'quantity': 3, 'price': 70000}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "trnsct_123.add_item(\"the\",1,3000)"
      ],
      "metadata": {
        "id": "J5XHAHekam2F",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "7d05a098-8b71-4283-f794-6a9969b61e35"
      },
      "execution_count": 599,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Barang yang anda beli adalah:\n",
            "{'name': 'cakue', 'quantity': 2, 'price': 50000}\n",
            "{'name': 'kopi', 'quantity': 3, 'price': 70000}\n",
            "{'name': 'the', 'quantity': 1, 'price': 3000}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "trnsct_123.update_item_name(\"the\",\"teh\")"
      ],
      "metadata": {
        "id": "nz1cGO7jFzON",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ec67303f-8fe3-456d-bf5e-1b2c281498a4"
      },
      "execution_count": 600,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "nama dari the berubah menjadi teh\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "trnsct_123.update_item_qty(\"teh\",5)"
      ],
      "metadata": {
        "id": "kn4C4MC4NGkR",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "68acc894-77dd-4cfe-b7ec-bb42478a7115"
      },
      "execution_count": 601,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Quantity teh berubah menjadi 5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "trnsct_123.update_item_price(\"teh\",15000)"
      ],
      "metadata": {
        "id": "OK2XHuFxNR5n"
      },
      "execution_count": 602,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "trnsct_123.delete_item(\"cakue\")"
      ],
      "metadata": {
        "id": "jg18evIGNcNX",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1811ad97-c7ec-49c6-9949-4dc67897e3fc"
      },
      "execution_count": 603,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "cakue berhasil di hapus!\n",
            "{'name': 'kopi', 'quantity': 3, 'price': 70000}\n",
            "{'name': 'teh', 'quantity': 5, 'price': 15000}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "total = trnsct_123.get_total()\n",
        "print(f'Total price: {total}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "y25zdn0HSrtU",
        "outputId": "8ea78669-21cc-4d8d-9bd4-08d348266fc2"
      },
      "execution_count": 565,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Total price: 285000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "trnsct_123.reset_transaction()"
      ],
      "metadata": {
        "id": "wcD5RlTWSv77",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ffdd7822-bc76-4d36-b796-ccfe2852567f"
      },
      "execution_count": 566,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "semua item berhasil dihapus!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "trnsct_123.check_order()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5yw7cYvUUh8s",
        "outputId": "1deeabde-b311-4f33-f201-fa37b9a05408"
      },
      "execution_count": 575,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Pemesanan sudah benar.\n",
            "+------+-----------+-------+\n",
            "| Nama | Kuantitas | Harga |\n",
            "+------+-----------+-------+\n",
            "| kopi |     3     | 70000 |\n",
            "| teh  |     5     | 15000 |\n",
            "+------+-----------+-------+\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "trnsct_123.total_price()"
      ],
      "metadata": {
        "id": "QxdjIs3uWt06",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5b817b22-1aab-40f1-f1b3-4c0c5dddaab2"
      },
      "execution_count": 576,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Total belanja Rp 270750 dengan diskon 5%.\n",
            "{'name': 'kopi', 'quantity': 3, 'price': 70000}\n",
            "{'name': 'teh', 'quantity': 5, 'price': 15000}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        " "
      ],
      "metadata": {
        "id": "-qdPbFI6oAaZ"
      },
      "execution_count": 149,
      "outputs": []
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}