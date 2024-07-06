def getEmail_US(full_name: str, dominio: str):
    """
    TODO: Retorna el correo del Usuario.
    Segun su nombre y el dominio del correo.

    Support: UserSimple
    """
    lt = full_name.split(" ")
    return f"{lt[0].lower()}.{lt[1].lower()}@{dominio}"
