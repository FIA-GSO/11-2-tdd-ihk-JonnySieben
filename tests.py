from main import *

def test__prozentausgabe(punkte, maxpunkte, erwartung):
    wert = punkte
    max = maxpunkte
    soll = erwartung

    ist = prozentwert(wert, max)

    assert ist == soll


def test__prozentausgabe_value_error(punkte, maxpunkte, erwartung):
    wert = punkte
    max = maxpunkte
    soll = erwartung

    ist = prozentwert(wert, max)

    with pytest.raises(ValueError):
        assert ist == soll

def test__prozentausgabe_type_error(punkte, maxpunkte, erwartung):
    wert = punkte
    max = maxpunkte
    soll = erwartung

    ist = prozentwert(wert, max)

    with pytest.raises(TypeError):
        assert ist == soll


def test__notenausgabe(prozentwert, erwartung):
    wert = prozentwert
    soll = erwartung

    ist = note(wert)

    assert ist == soll

def test__notenausgabe_value_error(prozentwert, erwartung):
    wert = prozentwert
    soll = erwartung

    ist = note(wert)

    with pytest.raises(ValueError):
        assert ist == soll


def test__notenausgabe_type_error(prozentwert, erwartung):
    wert = prozentwert
    soll = erwartung

    ist = note(wert)

    with pytest.raises(TypeError):
        assert ist == soll


# 100 Punkte
test__prozentausgabe(100, 100, 50)

# 0 Punkte
test__prozentausgabe(0, 100, 0)

# -1 punkte
test__prozentausgabe_value_error(-1, 100, 0)

# 101 Punkte
test__prozentausgabe_value_error(101, 100, 100)

# Punkte = "String"
test__prozentausgabe_type_error("null", 100, 0)

# Maxwert = "String"

#################################################

# 100%
test__notenausgabe(100, "sehr gut")

# 91%
test__notenausgabe(91, "gut")

# 6%
test__notenausgabe(80, "befriedigent")

# 66%
test__notenausgabe(66, "ausreichend")

# 29%
test__notenausgabe(29, "ungenügend")

# -1%
test__notenausgabe_value_error(-1, "ungenügend")

# 101%
test__notenausgabe_value_error(101, "sehr gut")

# Prozentwert = "string"
test__notenausgabe_type_error("null", "ungenügent")


#####################################################################

testdaten = [
    (100, 'sehr gut'),
    (92, 'sehr gut'),
    (91, 'gut'),
    (81, 'gut'),
    (80, 'befriedigend'),
    (67, 'befriedigend'),
    (66, 'ausreichend'),
    (50, 'ausreichend'),
    (49, 'mangelhaft'),
    (30, 'mangelhaft'),
    (29, 'ungenügend'),
    (0, 'ungenügend'),
]

throw = [
    (-1, ValueError),
    (101, ValueError),
    ('text', TypeError)
]

@pytest.mark.parametrize("prozent, erwartet", testdaten)
def test_bewerte(prozent, erwartet):
    assert prozentwert(prozent) == erwartet

@pytest.mark.parametrize("prozent, erwartet", throw)
def test_bewerte_Throw(prozent, erwartet):
    with pytest.raises(erwartet):
        notenstring(prozent)