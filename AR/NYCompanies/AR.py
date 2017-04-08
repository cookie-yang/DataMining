import Orange
data = Orange.data.Table("NYCompanies")
rules = Orange. associate .AssociationRulesSparseInducer(data, support=0.1, confidence=0.1)
for r in rules:
    print r
