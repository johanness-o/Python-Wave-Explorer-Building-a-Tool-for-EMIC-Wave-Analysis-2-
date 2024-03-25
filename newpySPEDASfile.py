import pyspedas
import csv
import pytplot
from pyspedas import mms_hpca_calc_anodes

# Load burst mode moments data
# hpca_vars = hpca(trange=['2015-10-16/13:05', '2015-10-16/13:10'], data_rate='brst', center_measurement=True)

# Plot the H+, O+ and He+ density
# tplot(['mms1_hpca_hplus_number_density',
#        'mms1_hpca_oplus_number_density',
#        'mms1_hpca_heplus_number_density'])
#
# # Plot the H+, O+ and He+ temperature
# tplot(['mms1_hpca_hplus_scalar_temperature',
#        'mms1_hpca_oplus_scalar_temperature',
#        'mms1_hpca_heplus_scalar_temperature'])
#
# # Plot the H+, O+ and He+ flow velocity¶
# tplot(['mms1_hpca_hplus_ion_bulk_velocity',
#        'mms1_hpca_oplus_ion_bulk_velocity',
#        'mms1_hpca_heplus_ion_bulk_velocity'])

# Plot the omni-directional flux for H+, O+ and He+, He++
# tplot(['mms1_hpca_hplus_flux_elev_0-360_spin',
#              'mms1_hpca_oplus_flux_elev_0-360_spin',
#              'mms1_hpca_heplus_flux_elev_0-360_spin',
#              'mms1_hpca_heplusplus_flux_elev_0-360_spin'])
# Load burst mode ion flux data
# ion_vars = hpca(trange=['2015-10-16/13:05', '2015-10-16/13:07'], datatype='ion', data_rate='brst',
#                 center_measurement=True)

# Average the flux over the full field of view (0-360)
# Robert's Code
# mms_fgm = pyspedas.mms.fgm(trange=['2015-10-16/13:05:30', '2015-10-16/13:07:30'], data_rate='brst')
# mms_fgm = pyspedas.mms.hpca(trange=['2015-10-16/13:05:30', '2015-10-16/13:07:30'])

# tplot(['mms1_fgm_b_gse_brst_l2', 'mms1_fgm_b_gsm_brst_l2',
#        'mms1_hpca_hplus_number_density','mms1_hpca_heplus_number_density',
#        'mms1_hpca_oplus_number_density'])

# Opening MMS Master list/ For Loop/ Initializing\
mms_hpca_calc_anodes(fov=[0, 360], probe='2')
with open('MMS_EMIC_wave_events_2015-2020_v6.csv') as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        if count == 1:
            start_time = [row[0] + '  ' + row[1]]
            end_time = [row[2] + '  ' + row[3]]
        elif count >= 2:
            start_time.append(row[0] + '  ' + row[1])
            end_time.append(row[2] + '  ' + row[3])

        count += 1

    # Load Calls FMG Data
    tracker = 1
    for index in range(len(start_time)):
        # This number needs to be updated each time I go through the code
        # can change tracker HERE
        if tracker > 2:
            print(start_time[index])
            print(end_time[index])
            # pyspedas.mms.fgm(trange=[start_time[index], end_time[index]], probe=1, time_clip = True)
            pyspedas.mms.fgm(trange=[pyspedas.time_string(pyspedas.time_double(start_time[index]) - 600),
                                     pyspedas.time_string(pyspedas.time_double(end_time[index]) + 600)], probe=1,
                             time_clip=True)
            # To load Magnetic Filed Data
            # pytplot.tplot(['mms1_fgm_b_gsm_srvy_l2_btot', 'mms1_fgm_b_gsm_srvy_l2_bvec'])
            pyspedas.mms.hpca(trange=[pyspedas.time_string(pyspedas.time_double(start_time[index])-600),
                                      pyspedas.time_string(pyspedas.time_double(end_time[index])+600)], datatype=['moments', 'ion'], probe=1)
            pyspedas.mms_hpca_calc_anodes(fov=[0, 360], probe=1)
            pyspedas.omni.data(trange=[pyspedas.time_string(pyspedas.time_double(start_time[index])-600),
                                       pyspedas.time_string(pyspedas.time_double(end_time[index])+600)])

            pytplot.options('mms1_hpca_hplus_flux_elev_0-360', 'Spec', 1)
            pytplot.options('mms1_hpca_hplus_flux_elev_0-360', 'zlog', 1)
            pytplot.options('mms1_hpca_heplusplus_flux_elev_0-360', 'Spec', 1)
            pytplot.options('mms1_hpca_heplusplus_flux_elev_0-360', 'zlog', 1)
            pytplot.options('mms1_hpca_oplus_flux_elev_0-360', 'Spec', 1)
            pytplot.options('mms1_hpca_oplus_flux_elev_0-360', 'zlog', 1)
            pytplot.options('mms1_hpca_heplus_flux_elev_0-360', 'Spec', 1)
            pytplot.options('mms1_hpca_heplus_flux_elev_0-360', 'zlog', 1)

            pytplot.timebar(start_time[index] + ':00', ['mms1_fgm_b_gsm_srvy_l2_btot', 'mms1_fgm_b_gsm_srvy_l2_bvec',
                                                        'mms1_hpca_hplus_flux_elev_0-360',
                                                        'mms1_hpca_hplus_number_density',
                                                        'mms1_hpca_heplusplus_flux_elev_0-360',
                                                        'mms1_hpca_heplusplus_number_density',
                                                        'mms1_hpca_oplus_flux_elev_0-360',
                                                        'mms1_hpca_oplus_number_density',
                                                        'mms1_hpca_heplus_flux_elev_0-360',
                                                        'mms1_hpca_heplus_number_density', 'AE_INDEX', 'SYM_H'])

            pytplot.timebar(end_time[index] + ':00', ['mms1_fgm_b_gsm_srvy_l2_btot', 'mms1_fgm_b_gsm_srvy_l2_bvec', 'mms1_hpca_hplus_flux_elev_0-360', 'mms1_hpca_hplus_number_density', 'mms1_hpca_heplusplus_flux_elev_0-360', 'mms1_hpca_heplusplus_number_density', 'mms1_hpca_oplus_flux_elev_0-360', 'mms1_hpca_oplus_number_density', 'mms1_hpca_heplus_flux_elev_0-360', 'mms1_hpca_heplus_number_density', 'AE_INDEX', 'SYM_H'])

            pytplot.tplot(['mms1_fgm_b_gsm_srvy_l2_btot', 'mms1_fgm_b_gsm_srvy_l2_bvec', 'mms1_hpca_hplus_flux_elev_0-360',
                 'mms1_hpca_hplus_number_density', 'mms1_hpca_heplusplus_flux_elev_0-360',
                 'mms1_hpca_heplusplus_number_density', 'mms1_hpca_oplus_flux_elev_0-360',
                 'mms1_hpca_oplus_number_density', 'mms1_hpca_heplus_flux_elev_0-360',
                 'mms1_hpca_heplus_number_density', 'AE_INDEX', 'SYM_H'])

        tracker += 1
    # in pytplot - Oxygen^+
    # pytplot.options('mms1_hpca_oplus_flux_elev_0-360', 'Spec', 1)
    # pytplot.options('mms1_hpca_oplus_flux_elev_0-360', 'zlog', 1)
    # pytplot.ylim('mms1_hpca_oplus_flux_elev_0-360', 10e1, 10e4)
    # pytplot.tplot(['mms1_hpca_oplus_flux_elev_0-360', 'mms1_hpca_oplus_number_density'])
    # Oxygen^+10e1 to 10e4.png

    # In pytplot - Hydrogen^+
    # pytplot.options('mms1_hpca_hplus_flux_elev_0-360', 'Spec', 1)
    # pytplot.options('mms1_hpca_hplus_flux_elev_0-360', 'zlog', 1)
    # pytplot.ylim('mms1_hpca_hplus_flux_elev_0-360', 10e1, 10e4)
    # pytplot.tplot(['mms1_hpca_hplus_flux_elev_0-360', 'mms1_hpca_hplus_number_density'])

    # Changes Color
    # pytplot.options('mms1_hpca_hplus_flux_elev_0-360', 'colormap', 'PRGn', 'RdBu')

    # In pytplot - Helium^+
    # pytplot.options('mms1_hpca_heplus_flux_elev_0-360', 'Spec', 1)
    # pytplot.options('mms1_hpca_heplus_flux_elev_0-360', 'zlog', 1)
    # pytplot.tplot(['mms1_hpca_heplus_flux_elev_0-360', 'mms1_hpca_heplus_number_density'])
    # pytplot.ylim('mms1_hpca_heplus_flux_elev_0-360', 10e1, 10e4)
    # Helium^+10e1 to 105e5pytplot

    # In pytplot - Helium^++
    # pytplot.options('mms1_hpca_heplusplus_flux_elev_0-360', 'Spec', 1)
    # pytplot.options('mms1_hpca_heplusplus_flux_elev_0-360', 'zlog', 1)
    # pytplot.tplot(['mms1_hpca_heplusplus_flux_elev_0-360', 'mms1_hpca_heplus_number_density'])
    # pytplot.ylim('mms1_hpca_heplusplus_flux_elev_0-360', 10e1, 10e4)
    # Helium^+10e1 to 105e5pytplot

    # Combine into one call - All data
    # Possibly use main.py to arrange subplots

    # Oxygen^+ - Spin
    # pytplot.options('mms1_hpca_oplus_flux_elev_0-360_spin', 'Spec', 1)
    # pytplot.options('mms1_hpca_oplus_flux_elev_0-360_spin', 'zlog', 1)
    # # pytplot.ylim('mms1_hpca_oplus_flux_elev_0-360_spin', 10e1, 10e4)
    # pytplot.tplot(['mms1_hpca_oplus_flux_elev_0-360_spin', 'mms1_hpca_oplus_number_density'])
    #
    # # Hydrogen^+ - Spin
    # pytplot.options('mms1_hpca_hplus_flux_elev_0-360_spin', 'Spec', 1)
    # pytplot.options('mms1_hpca_hplus_flux_elev_0-360_spin', 'zlog', 1)
    # # pytplot.ylim('mms1_hpca_hplus_flux_elev_0-360_spin', 10e1, 10e4)
    # pytplot.tplot(['mms1_hpca_hplus_flux_elev_0-360_spin', 'mms1_hpca_hplus_number_density'])
    #
    # # Helium^+ - Spin
    # pytplot.options('mms1_hpca_heplus_flux_elev_0-360_spin', 'Spec', 1)
    # pytplot.options('mms1_hpca_heplus_flux_elev_0-360_spin', 'zlog', 1)
    # pytplot.tplot(['mms1_hpca_heplus_flux_elev_0-360_spin', 'mms1_hpca_heplus_number_density'])
    # # pytplot.ylim('mms1_hpca_heplus_flux_elev_0-360_spin', 10e1, 10e4)
    #
    # # Helium ^ ++ - Spin
    # pytplot.options('mms1_hpca_heplusplus_flux_elev_0-360_spin', 'Spec', 1)
    # pytplot.options('mms1_hpca_heplusplus_flux_elev_0-360_spin', 'zlog', 1)
    # pytplot.tplot(['mms1_hpca_heplusplus_flux_elev_0-360_spin', 'mms1_hpca_heplus_number_density'])
    # # pytplot.ylim('mms1_hpca_heplusplus_flux_elev_0-360_spin', 10e1, 10e4)
    #
    #
    # pytplot.tplot(['mms1_hpca_hplus_flux_elev_0-360_spin',
    #          'mms1_hpca_oplus_flux_elev_0-360_spin',
    #          'mms1_hpca_heplus_flux_elev_0-360_spin',
    #          'mms1_hpca_heplusplus_flux_elev_0-360_spin'])
    # pytplot.tplot(['mms1_fgm_b_gsm_srvy_l2_btot', 'mms1_fgm_b_gsm_srvy_l2_bvec', 'mms1_hpca_hplus_flux_elev_0-360', 'mms1_hpca_hplus_number_density', 'mms1_hpca_heplusplus_flux_elev_0-360', 'mms1_hpca_heplusplus_number_density', 'mms1_hpca_oplus_flux_elev_0-360', 'mms1_hpca_oplus_number_density', 'mms1_hpca_heplus_flux_elev_0-360', 'mms1_hpca_heplus_number_density'])