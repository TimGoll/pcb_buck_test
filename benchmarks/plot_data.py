import pathlib, pandas
import plt

folder = str(pathlib.Path(__file__).parent.resolve())

### XL1509-ADJE1
xl_065 = pandas.read_csv(folder + "/data/xl_in_6.5.csv")
xl_120 = pandas.read_csv(folder + "/data/xl_in_12.0.csv")
xl_310 = pandas.read_csv(folder + "/data/xl_in_31.0.csv")

xl_065_eff = (xl_065["U_out"][1:] * xl_065["I_out"][1:]) / (xl_065["U_in"][1:] * xl_065["I_in"][1:])
xl_120_eff = (xl_120["U_out"][1:] * xl_120["I_out"][1:]) / (xl_120["U_in"][1:] * xl_120["I_in"][1:])
xl_310_eff = (xl_310["U_out"][1:] * xl_310["I_out"][1:]) / (xl_310["U_in"][1:] * xl_310["I_in"][1:])

plt.plt(
    [xl_065["I_out"], xl_120["I_out"], xl_310["I_out"]],
    [xl_065["U_out"], xl_120["U_out"], xl_310["U_out"]],
    ["U_in = 6.5V", "U_in = 12.0V", "U_in = 31.0V"],
    "output current (A)",
    "output voltage (V)",
    (0, 5.5),
    folder + "/plots/xl1509_volts.png"
)

plt.plt(
    [xl_065["I_out"][1:], xl_120["I_out"][1:], xl_310["I_out"][1:]],
    [xl_065_eff, xl_120_eff, xl_310_eff],
    ["U_in = 6.5V", "U_in = 12.0V", "U_in = 31.0V"],
    "output current (A)",
    "efficiency",
    (0, 1.0),
    folder + "/plots/xl1509_eff.png"
)

### MT2492
mt_065 = pandas.read_csv(folder + "/data/mt_in_6.5.csv")
mt_120 = pandas.read_csv(folder + "/data/mt_in_12.0.csv")
mt_160 = pandas.read_csv(folder + "/data/mt_in_16.0.csv")

mt_065_eff = (mt_065["U_out"][1:] * mt_065["I_out"][1:]) / (mt_065["U_in"][1:] * mt_065["I_in"][1:])
mt_120_eff = (mt_120["U_out"][1:] * mt_120["I_out"][1:]) / (mt_120["U_in"][1:] * mt_120["I_in"][1:])
mt_160_eff = (mt_160["U_out"][1:] * mt_160["I_out"][1:]) / (mt_160["U_in"][1:] * mt_160["I_in"][1:])

plt.plt(
    [mt_065["I_out"], mt_120["I_out"], mt_160["I_out"]],
    [mt_065["U_out"], mt_120["U_out"], mt_160["U_out"]],
    ["U_in = 6.5V", "U_in = 12.0V", "U_in = 16.0V"],
    "output current (A)",
    "output voltage (V)",
    (0, 5.5),
    folder + "/plots/mt2492_volts.png"
)

plt.plt(
    [mt_065["I_out"][1:], mt_120["I_out"][1:], mt_160["I_out"][1:]],
    [mt_065_eff, mt_120_eff, mt_160_eff],
    ["U_in = 6.5V", "U_in = 12.0V", "U_in = 16.0V"],
    "output current (A)",
    "efficiency",
    (0, 1.0),
    folder + "/plots/mt2492_eff.png"
)

### TPS52160DSG - pos
tps_p_065 = pandas.read_csv(folder + "/data/tps_pos_in_6.5.csv")
tps_p_100 = pandas.read_csv(folder + "/data/tps_pos_in_10.0.csv")
tps_p_170 = pandas.read_csv(folder + "/data/tps_pos_in_17.0.csv")

tps_p_065_eff = (tps_p_065["U_out"][1:] * tps_p_065["I_out"][1:]) / (tps_p_065["U_in"][1:] * tps_p_065["I_in"][1:])
tps_p_100_eff = (tps_p_100["U_out"][1:] * tps_p_100["I_out"][1:]) / (tps_p_100["U_in"][1:] * tps_p_100["I_in"][1:])
tps_p_170_eff = (tps_p_170["U_out"][1:] * tps_p_170["I_out"][1:]) / (tps_p_170["U_in"][1:] * tps_p_170["I_in"][1:])

plt.plt(
    [tps_p_065["I_out"], tps_p_100["I_out"], tps_p_170["I_out"]],
    [tps_p_065["U_out"], tps_p_100["U_out"], tps_p_170["U_out"]],
    ["U_in = 6.5V", "U_in = 10.0V", "U_in = 17.0V"],
    "output current (A)",
    "output voltage (V)",
    (0, 5.5),
    folder + "/plots/tps62160_pos_volts.png"
)

plt.plt(
    [tps_p_065["I_out"][1:], tps_p_100["I_out"][1:], tps_p_170["I_out"][1:]],
    [tps_p_065_eff, tps_p_100_eff, tps_p_170_eff],
    ["U_in = 6.5V", "U_in = 10.0V", "U_in = 17.0V"],
    "output current (A)",
    "efficiency",
    (0, 1.0),
    folder + "/plots/tps62160_pos_eff.png"
)

### TPS52160DSG - neg
tps_n_050 = pandas.read_csv(folder + "/data/tps_neg_in_5.0.csv")
tps_n_055 = pandas.read_csv(folder + "/data/tps_neg_in_5.5.csv")
tps_n_060 = pandas.read_csv(folder + "/data/tps_neg_in_6.0.csv")
tps_n_100 = pandas.read_csv(folder + "/data/tps_neg_in_10.0.csv")

tps_n_050_eff = -1 * (tps_n_050["U_out"][1:] * tps_n_050["I_out"][1:]) / (tps_n_050["U_in"][1:] * tps_n_050["I_in"][1:])
tps_n_055_eff = -1 * (tps_n_055["U_out"][1:] * tps_n_055["I_out"][1:]) / (tps_n_055["U_in"][1:] * tps_n_055["I_in"][1:])
tps_n_060_eff = -1 * (tps_n_060["U_out"][1:] * tps_n_060["I_out"][1:]) / (tps_n_060["U_in"][1:] * tps_n_060["I_in"][1:])
tps_n_100_eff = -1 * (tps_n_100["U_out"][1:] * tps_n_100["I_out"][1:]) / (tps_n_100["U_in"][1:] * tps_n_100["I_in"][1:])

plt.plt(
    [tps_n_050["I_out"], tps_n_055["I_out"], tps_n_060["I_out"], tps_n_100["I_out"]],
    [tps_n_050["U_out"], tps_n_055["U_out"], tps_n_060["U_out"], tps_n_100["U_out"]],
    ["U_in = 5.0V", "U_in = 5.5V", "U_in = 6.0V", "U_in = 10V"],
    "output current (A)",
    "output voltage (V)",
    (0, -5.5),
    folder + "/plots/tps62160_neg_volts.png"
)

plt.plt(
    [tps_n_050["I_out"][1:], tps_n_055["I_out"][1:], tps_n_060["I_out"][1:], tps_n_100["I_out"][1:]],
    [tps_n_050_eff, tps_n_055_eff, tps_n_060_eff, tps_n_100_eff],
    ["U_in = 5.0V", "U_in = 5.5V", "U_in = 6.0V", "U_in = 10V"],
    "output current (A)",
    "efficiency",
    (0, 1.0),
    folder + "/plots/tps62160_neg_eff.png"
)
