import obspyNN

sds_root = "/mnt/DATA"
sfile_list = obspyNN.io.read_sfile_list("/mnt/tf_data/sfilelist")

stream = obspyNN.io.load_stream(sfile_list, sds_root, plot=False)
stream.write("data.pkl", format="PICKLE")