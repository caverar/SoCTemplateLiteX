GPIO
====

Register Listing for GPIO
-------------------------

+------------------------------------------+-------------------------------------+
| Register                                 | Address                             |
+==========================================+=====================================+
| :ref:`GPIO_LED_REG <GPIO_LED_REG>`       | :ref:`0xf0000000 <GPIO_LED_REG>`    |
+------------------------------------------+-------------------------------------+
| :ref:`GPIO_SW_REG <GPIO_SW_REG>`         | :ref:`0xf0000004 <GPIO_SW_REG>`     |
+------------------------------------------+-------------------------------------+
| :ref:`GPIO_EV_STATUS <GPIO_EV_STATUS>`   | :ref:`0xf0000008 <GPIO_EV_STATUS>`  |
+------------------------------------------+-------------------------------------+
| :ref:`GPIO_EV_PENDING <GPIO_EV_PENDING>` | :ref:`0xf000000c <GPIO_EV_PENDING>` |
+------------------------------------------+-------------------------------------+
| :ref:`GPIO_EV_ENABLE <GPIO_EV_ENABLE>`   | :ref:`0xf0000010 <GPIO_EV_ENABLE>`  |
+------------------------------------------+-------------------------------------+

GPIO_LED_REG
^^^^^^^^^^^^

`Address: 0xf0000000 + 0x0 = 0xf0000000`


    .. wavedrom::
        :caption: GPIO_LED_REG

        {
            "reg": [
                {"name": "led_reg[3:0]", "bits": 4},
                {"bits": 28},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


GPIO_SW_REG
^^^^^^^^^^^

`Address: 0xf0000000 + 0x4 = 0xf0000004`


    .. wavedrom::
        :caption: GPIO_SW_REG

        {
            "reg": [
                {"name": "sw_reg[3:0]", "bits": 4},
                {"bits": 28},
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


GPIO_EV_STATUS
^^^^^^^^^^^^^^

`Address: 0xf0000000 + 0x8 = 0xf0000008`

    Se activa cuando hay un flanco de subida en los switch

    .. wavedrom::
        :caption: GPIO_EV_STATUS

        {
            "reg": [
                {"name": "switchIRQ",  "bits": 1},
                {"bits": 31}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


+-------+-----------+----------------------------------+
| Field | Name      | Description                      |
+=======+===========+==================================+
| [0]   | SWITCHIRQ | Level of the ``switchIRQ`` event |
+-------+-----------+----------------------------------+

GPIO_EV_PENDING
^^^^^^^^^^^^^^^

`Address: 0xf0000000 + 0xc = 0xf000000c`

    Se activa cuando hay un flanco de subida en los switch

    .. wavedrom::
        :caption: GPIO_EV_PENDING

        {
            "reg": [
                {"name": "switchIRQ",  "bits": 1},
                {"bits": 31}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


+-------+-----------+--------------------------------------------------------+
| Field | Name      | Description                                            |
+=======+===========+========================================================+
| [0]   | SWITCHIRQ | Se activa cuando hay un flanco de subida en los switch |
+-------+-----------+--------------------------------------------------------+

GPIO_EV_ENABLE
^^^^^^^^^^^^^^

`Address: 0xf0000000 + 0x10 = 0xf0000010`

    Se activa cuando hay un flanco de subida en los switch

    .. wavedrom::
        :caption: GPIO_EV_ENABLE

        {
            "reg": [
                {"name": "switchIRQ",  "bits": 1},
                {"bits": 31}
            ], "config": {"hspace": 400, "bits": 32, "lanes": 4 }, "options": {"hspace": 400, "bits": 32, "lanes": 4}
        }


+-------+-----------+-------------------------------------------------+
| Field | Name      | Description                                     |
+=======+===========+=================================================+
| [0]   | SWITCHIRQ | Write a ``1`` to enable the ``switchIRQ`` Event |
+-------+-----------+-------------------------------------------------+

