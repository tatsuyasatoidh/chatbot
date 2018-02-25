from unmo import Unmo

def _build_prompt(unmo):
    """AIインスタンスを取り、AIとResponderの名前を整形して返す"""
    return '{name}> '.format(name=unmo.name,
                                         responder=unmo.responder_name)

def main():
    print('CHAT START')
    proto = Unmo('ボットの兄貴')
    while True:
        text = input('> ')
        if not text:
            break

        response = proto.dialogue(text)
        print('{prompt}{response}'.format(prompt=_build_prompt(proto),
                                          response=response))
    proto.save()
