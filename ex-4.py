# Ex-5
# Extract filenames that has txt as extension
filenames = ['file1.txt', 'file2.txt', 'file3.pdf', 'file4.pdf']

txtfiles = [i for i in filenames if i.endswith('txt')]


# for f in filenames:
#     if 'txt' in f:
#         txtfiles.append(f)


print(txtfiles)