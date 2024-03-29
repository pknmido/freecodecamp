class Category:

  def __init__(self, name) -> None:
    self.ledger = []
    self.name = name
    self.amount = 0.00
    self.overall_amount = 0.0

  def check_funds(self, amount):
    if amount > self.amount:
      return False
    else:
      return True

  def deposit(self, amount, description=''):
    self.amount += amount
    self.overall_amount += amount
    x = {'amount': amount, 'description': description}
    self.ledger.append(x)
    return

  def withdraw(self, amount, description=''):
    if self.check_funds(amount) == True:
      x = {'amount': amount * -1, 'description': description}
      self.ledger.append(x)
      self.amount -= amount
      return True
    else:
      return False

  def get_balance(self):
    return self.amount

  def transfer(self, amount, categ):
    x = self.withdraw(amount, f'Transfer to {categ.name}')
    categ.deposit(amount, f'Transfer from {self.name}')
    return x

  def __str__(self) -> str:
    x = self.name.center(30, '*')
    z = ''
    for i in self.ledger:
      try:
        a = format(float(i['amount']), '.2f')
        b = i['description']
        try:
          b = b[:23]
        except:
          pass
        z += f'{b}{a.rjust(30 - len(b))}\n'
      except:
        z += f'{str(i).rjust(30)}\n'
    total = format(self.amount, '.2f')
    return f'{x}\n{z}Total: {total}'


def create_spend_chart(lst):
  lines = ''
  z = 0
  for categ in lst:
    z += (categ.overall_amount - categ.amount)
  for i in range(-10, 1):
    lines += f'\n{str((-i * 10)).rjust(3)}| '
    for categ in lst:
      x = ((categ.overall_amount - categ.amount) * 100 / z).__floor__()
      if x >= (-i * 10):
        lines += f'{"o  "}'
      else:
        lines += '   '
  y = int(len(lines) / 11) - 2
  z = ''
  for j in range(max_len(lst)):
    for categ in lst:
      try:
        z += f'{categ.name[j]}  '
      except:
        z += '   '
    if j != max_len(lst) - 1:
      z += '\n     '
  return f'Percentage spent by category{lines}\n    {"-"*(y-3)}\n     {z}'

def max_len(lst):
  x = []
  for i in lst:
    x.append(len(i.name))
  return max(x)
