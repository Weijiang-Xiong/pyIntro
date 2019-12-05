def findPayment(loan:float, r:float, m:int):
    """
    Returns the monthly payment for a mortgage of size
    loan at a monthly rate of r for m months
    """ 
    return loan*((r*(1+r)**m)/((1+r)**m - 1))

class Mortgage(object):
    """
        abstract class for building diferent kinds of mortgages"""
    def __init__(self, loan, annRate, months):
        self.loan = loan
        self.rate = annRate/12
        self.months = months
        self.paid = [0.0]
        self.outstanding = [loan]
        self.payment = findPayment(loan, self.rate, self.months)
        self.legend = None

    def makePayment(self):
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1]*self.rate
        self.outstanding.append(self.outstanding[-1] - reduction)

    def getTotalPaid(self):
        """Return the total amount paid so far"""
        return sum(self.paid)

    def __str__(self):
        return self.legend

class Fixed(Mortgage):
    def __init__(self, loan, annRate, months):
        Mortgage.__init__(self, loan, annRate, months)
        self.legend = 'Fixed, ' + str(round(annRate*100/12, 2)) + '%'

class FixedWithPts(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan*(pts/100)]
        self.legend = 'Fixed, ' + str(round(r*100, 2)) + '%, '+ str(pts) + ' points'
class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r/12
        self.legend = str(teaserRate*100) + '% for ' + str(self.teaserMonths) + ' months, then ' + str(round(r*100, 2)) + '%'
    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1: 
            self.rate = self.nextRate
            self.payment = findPayment(self.outstanding[-1],
            self.rate,
            self.months - self.teaserMonths)
        Mortgage.makePayment(self)

        







