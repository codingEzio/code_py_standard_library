import dis
import sys
import textwrap
import timeit

tips = ''' 
    use this file to 
        test the `dis_08_test_slow_loop.py'
        don't add the extension! (.py)
    example command
        python -m dis_07_test_loop dis_08_test_slow_loop
'''

module_name = sys.argv[1]

module = __import__(module_name)
Dictionary = module.Dictionary

dis.dis(Dictionary.load_data)

print()

t = timeit.Timer(
    'd = Dictionary(words)',
    textwrap.dedent("""
    from {module_name} import Dictionary
    words = [
        l.strip() for l in open('/usr/share/dict/words', 'rt')
    ]
    """).format(module_name=module_name)
)

iterations = 10

print('TIME: {:0.4f}'.format(
    t.timeit(iterations) / iterations
))
