
from mhcflurry import Class1BindingPredictor

def test_A1_Titin_epitope():
    # Test the A1 Titin epitope ESDPIVAQY from
    #   Identification of a Titin-Derived HLA-A1-Presented Peptide
    #   as a Cross-Reactive Target for Engineered MAGE A3-Directed
    #   T Cells
    model = Class1BindingPredictor.from_allele_name("HLA-A*01:01")
    ic50s = model.predict_peptides_ic50(["ESDPIVAQY"])
    print(ic50s)
    assert len(ic50s) == 1
    ic50 = ic50s[0]
    assert ic50 <= 500

def test_A1_MAGE_epitope():
    # Test the A1 MAGE epitope EVDPIGHLY from
    #   Identification of a Titin-Derived HLA-A1-Presented Peptide
    #   as a Cross-Reactive Target for Engineered MAGE A3-Directed
    #   T Cells
    model = Class1BindingPredictor.from_allele_name("HLA-A*01:01")
    ic50s = model.predict_peptides_ic50(["EVDPIGHLY"])
    print(ic50s)
    assert len(ic50s) == 1
    ic50 = ic50s[0]
    assert ic50 <= 500

def test_A2_HIV_epitope():
    # Test the A2 HIV epitope SLYNTVATL from
    #    The HIV-1 HLA-A2-SLYNTVATL Is a Help-Independent CTL Epitope
    model = Class1BindingPredictor.from_allele_name("HLA-A*02:01")
    ic50s = model.predict_peptides_ic50(["SLYNTVATL"])
    print(ic50s)
    assert len(ic50s) == 1
    ic50 = ic50s[0]
    assert ic50 <= 500


if __name__ == "__main__":
    test_A1_Titin_epitope()
    test_A1_MAGE_epitope()
    test_A2_HIV_epitope()