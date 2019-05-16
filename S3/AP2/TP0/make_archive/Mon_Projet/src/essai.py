def note_finale (ds1,ds2,tp,prj):
    """
    renvoie la note finale en AP2.

    :param ds1: note de DS1
    :type ds1: float
    :param ds2: note de DS2
    :type ds2: float
    :param tp: note de TP
    :type tp: float
    :param prj: note de projet
    :type prj: float
    :return: note finale
    :rtype: float
    :UC: 0 <= ds1,ds2,tp,prj <= 20
    :Example:

    >>> note_finale (10,12,13,14)
    12.8
    """
    assert 0 <= ds1 <= 20, 'pas une note'
    assert 0 <= ds2 <= 20, 'pas une note'
    assert 0 <= tp <= 20, 'pas une note'
    assert 0 <= prj <= 20, 'pas une note'
    ecrit = max (ds2, (ds1 + 2*ds2)/3)
    return 0.5*ecrit + 0.2*tp + 0.3*prj
