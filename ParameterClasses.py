from enum import Enum
import InputData as Data


class HealthStats(Enum):

    WELL = 0
    DEAD_OTHER = 1
    TIA = 2
    POST_TIA = 3
    MILD_STROKE = 4
    POST_MILD_STROKE = 5
    MODERATE_SEVERE_STROKE = 6
    POST_MODERATE_SEVERE_STROKE = 7
    DEAD_STROKE = 8


class Therapies(Enum):

    WARFARIN = 0
    DABIGATRAN_110MG = 1
    DABIGATRAN_150MG = 2


class ParametersFixed():
    def __init__(self, therapy):

        # selected therapy
        self._therapy = therapy

        # simulation time step
        self._delta_t = Data.DELTA_T

        self._adjDiscountRate = Data.DISCOUNT * Data.DELTA_T

        # initial health state
        self._initialHealthState = HealthStats.WELL

        # annual treatment cost
        if self._therapy == Therapies.WARFARIN:
            self._annualTreatmentCost = Data.WARFARIN_ANNUAL_COST
        if self._therapy == Therapies.DABIGATRAN_110MG:
            self._annualTreatmentCost = Data.DABIGATRAN_110MG_ANNUAL_COST
        if self._therapy == Therapies.DABIGATRAN_150MG:
            self._annualTreatmentCost = Data.DABIGATRAN_150MG_ANNUAL_COST

        # transition probability matrix of the selected therapy
        self._prob_matrix = []
        # treatment relative risk
        self._treatmentRR = 0

        # calculate transition probabilities depending of which therapy options is in use
        if therapy == Therapies.WARFARIN:
            self._prob_matrix = Data.TRANS_MATRIX_WARFARIN
        if therapy == Therapies.DABIGATRAN_110MG:
            self._prob_matrix = Data.TRANS_MATRIX_DABIGATRAN_110MG
        if therapy == Therapies.DABIGATRAN_150MG:
            self._prob_matrix = Data.TRANS_MATRIX_DABIGATRAN_150MG

        self._annualStateCosts = Data.HEALTH_COST
        self._annualStateUtilities = Data.HEALTH_UTILITY

    def get_initial_health_state(self):
        return self._initialHealthState

    def get_delta_t(self):
        return self._delta_t

    def get_adj_discount_rate(self):
        return self._adjDiscountRate

    def get_transition_prob(self, state):
        return self._prob_matrix[state.value]

    def get_annual_state_cost(self, state):
        if state == HealthStats.DEAD_OTHER or state == HealthStats.DEAD_STROKE:
            return 0
        else:
            return self._annualStateCosts[state.value]

    def get_annual_state_utility(self, state):
        if state == HealthStats.DEAD_OTHER or state == HealthStats.DEAD_STROKE:
            return 0
        else:
            return self._annualStateUtilities[state.value]

    def get_annual_treatment_cost(self):
        return self._annualTreatmentCost



