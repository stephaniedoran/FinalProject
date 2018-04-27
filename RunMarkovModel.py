import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

# create and simulate cohort
warfarin_cohort = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.WARFARIN)

warfarin_simOutputs = warfarin_cohort.simulate()

# graph survival curve
PathCls.graph_sample_path(
    sample_path=warfarin_simOutputs.get_survival_curve(),
    title='Survival curve, Warfarin',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# graph histogram of survival times
Figs.graph_histogram(
    data=warfarin_simOutputs.get_survival_times(),
    title='Survival times of patients with Stroke, Warfarin',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)

# graph histogram of number of strokes
Figs.graph_histogram(
    data=warfarin_simOutputs.get_if_developed_stroke(),
    title='Number of Strokes per Patient, Warfarin',
    x_label='Strokes',
    y_label='Counts',
    bin_width=1
)

# print outcomes (means and CIs)
SupportMarkov.print_outcomes(warfarin_simOutputs, 'Warfarin:')


# create and simulate cohort
dabigatran_110_cohort = MarkovCls.Cohort(
    id=2,
    therapy=P.Therapies.DABIGATRAN_110MG)

dabigatran_110_simOutputs = dabigatran_110_cohort.simulate()

# graph survival curve
PathCls.graph_sample_path(
    sample_path=dabigatran_110_simOutputs.get_survival_curve(),
    title='Survival curve, Dabigatran 110',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# graph histogram of survival times
Figs.graph_histogram(
    data=dabigatran_110_simOutputs.get_survival_times(),
    title='Survival times of patients with Stroke, Dabigatran 110',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)

# graph histogram of number of strokes
Figs.graph_histogram(
    data=dabigatran_110_simOutputs.get_if_developed_stroke(),
    title='Number of Strokes per Patient, Dabigatran 110',
    x_label='Strokes',
    y_label='Counts',
    bin_width=1
)

# print outcomes (means and CIs)
SupportMarkov.print_outcomes(dabigatran_110_simOutputs, 'Dabigatran 110:')



# create and simulate cohort
dabigatran_150_cohort = MarkovCls.Cohort(
    id=3,
    therapy=P.Therapies.DABIGATRAN_150MG)

dabigatran_150_simOutputs = dabigatran_150_cohort.simulate()

# graph survival curve
PathCls.graph_sample_path(
    sample_path=dabigatran_150_simOutputs.get_survival_curve(),
    title='Survival curve, Dabigatran 150',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# graph histogram of survival times
Figs.graph_histogram(
    data=dabigatran_150_simOutputs.get_survival_times(),
    title='Survival times of patients with Stroke, Dabigatran 150',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)

# graph histogram of number of strokes
Figs.graph_histogram(
    data=dabigatran_150_simOutputs.get_if_developed_stroke(),
    title='Number of Strokes per Patient, Dabigatran 150',
    x_label='Strokes',
    y_label='Counts',
    bin_width=1
)

# print outcomes (means and CIs)
SupportMarkov.print_outcomes(warfarin_simOutputs, 'Dabigatran 150:')
