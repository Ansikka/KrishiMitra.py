def test_import_main():
    try:
        import krishimitra_app
    except Exception as e:
        assert False, f"Import failed: {e}" 