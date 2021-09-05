import json

class pydeequDynamicParser:
    pydeequ_check_instance = None
    user_checks = None
    functions_map = None

    def __init__(self, pydeequ_check_instance, user_checks):
        self.pydeequ_check_instance = pydeequ_check_instance
        self.user_checks = json.loads(user_checks) if type(
            user_checks) is str else user_checks
        self.functions_map = {"satisfies": self.dq_satisfies,
                              "isUnique": self.dq_isunique,
                              "containsEmail": self.dq_contains_email,
                              "isComplete": self.dq_is_complete,
                              "areComplete": self.dq_are_complete,
                              "containsCreditCardNumber": self.dq_contains_credit_card_number,
                              "containsSocialSecurityNumber": self.dq_contains_social_security_number,
                              "containsURL": self.dq_contains_url,
                              "hasApproxCountDistinct": self.dq_has_approx_count_distinct,
                              "hasApproxQuantile": self.dq_has_approx_quantile,
                              "hasCompleteness": self.dq_has_completeness,
                              "hasCorrelation": self.dq_has_correlation,
                              "hasDistinctness": self.dq_has_distinctness,
                              "hasEntropy": self.dq_has_entropy,
                              "hasMax": self.dq_has_max,
                              "hasMaxLength": self.dq_has_max_length,
                              "hasMean": self.dq_has_mean,
                              "hasMin": self.dq_has_min,
                              "hasMinLength": self.dq_has_min_length,
                              "hasMutualInformation": self.dq_has_mutual_information,
                              "hasSize": self.dq_has_size,
                              "hasStandardDeviation": self.dq_has_standard_deviation,
                              "hasSum": self.dq_has_sum,
                              "hasUniqueValueRatio": self.dq_has_unique_value_ratio,
                              "hasUniqueness": self.dq_has_uniqueness,
                              "haveAnyCompleteness": self.dq_have_any_completeness,
                              "haveCompleteness": self.dq_have_completeness,
                              "isContainedIn": self.dq_is_contained_in,
                              "isGreaterThan": self.dq_is_greater_than,
                              "isGreaterThanOrEqualTo": self.dq_is_greater_than_or_equal_to,
                              "isLessThan": self.dq_is_less_than,
                              "isLessThanOrEqualTo": self.dq_is_less_than_or_equal_to,
                              "isNonNegative": self.dq_is_non_negative,
                              "isPositive": self.dq_is_positive,
                              "hasNumberOfDistinctValues": self.dq_has_number_of_distinct_values,
                              "hasHistogramValues": self.dq_has_histogram_values,
                              "hasPattern": self.dq_has_pattern,
                              "hasDataType": self.dq_has_data_type,
                              "kllSketchSatisfies": self.dq_kll_sketch_satisfies}

    @staticmethod
    def validate_eval(function):
        if function is None:
            return function
        else:
            return eval(function)

    def dq_satisfies(self, columnCondition, constraintName, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.satisfies(
            columnCondition, constraintName, self.validate_eval(assertion), hint)

    def dq_isunique(self, column, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.isUnique(
            column, hint)

    def dq_contains_email(self, column, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.containsEmail(
            column, self.validate_eval(assertion), hint)

    def dq_is_complete(self, column, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.isComplete(
            column, hint)

    def dq_are_complete(self, columns, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.areComplete(
            columns, hint)

    def dq_contains_credit_card_number(self, column, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.containsCreditCardNumber(
            column, self.validate_eval(assertion), hint)

    def dq_contains_social_security_number(self, column, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.containsSocialSecurityNumber(
            column, self.validate_eval(assertion), hint)

    def dq_contains_url(self, column, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.containsURL(
            column, self.validate_eval(assertion), hint)

    def dq_has_approx_count_distinct(self, column, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasApproxCountDistinct(
            column, self.validate_eval(assertion), hint)

    def dq_has_approx_quantile(self, column, quantile, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasApproxQuantile(
            column, quantile, self.validate_eval(assertion), hint)

    def dq_has_completeness(self, column, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasCompleteness(
            column, self.validate_eval(assertion), hint)

    def dq_has_correlation(self, columnA, columnB, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasCorrelation(
            columnA, columnB, self.validate_eval(assertion), hint)

    def dq_has_distinctness(self, columns, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasDistinctness(
            columns, self.validate_eval(assertion), hint)

    def dq_has_entropy(self, column, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasEntropy(
            column, self.validate_eval(assertion), hint)

    def dq_has_max(self, column, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasMax(
            column, self.validate_eval(assertion), hint)

    def dq_has_max_length(self, column, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasMaxLength(
            column, self.validate_eval(assertion), hint)

    def dq_has_mean(self, column, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasMean(
            column, self.validate_eval(assertion), hint)

    def dq_has_min(self, column, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasMin(
            column, self.validate_eval(assertion), hint)

    def dq_has_min_length(self, column, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasMinLength(
            column, self.validate_eval(assertion), hint)

    def dq_has_mutual_information(self, columnA, columnB, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasMutualInformation(
            columnA, columnB, self.validate_eval(assertion), hint)      

    def dq_has_size(self, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasSize(
            self.validate_eval(assertion), hint)

    def dq_has_standard_deviation(self, column, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasStandardDeviation(
            column, self.validate_eval(assertion), hint)

    def dq_has_sum(self, column, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasSum(
            column, self.validate_eval(assertion), hint)

    def dq_has_unique_value_ratio(self, columns, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasUniqueValueRatio(
            columns, self.validate_eval(assertion), hint)

    def dq_has_uniqueness(self, columns, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasUniqueness(
            columns, self.validate_eval(assertion), hint)

    def dq_have_any_completeness(self, columns, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.haveAnyCompleteness(
            columns, self.validate_eval(assertion), hint)

    def dq_have_completeness(self, columns, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.haveCompleteness(
            columns, self.validate_eval(assertion), hint)

    def dq_is_contained_in(self, column, allowed_values):
        self.pydeequ_check_instance = self.pydeequ_check_instance.isContainedIn(
            column, allowed_values)

    def dq_is_greater_than(self, columnA, columnB, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.isGreaterThan(
            columnA, columnB, self.validate_eval(assertion), hint)

    def dq_is_greater_than_or_equal_to(self, columnA, columnB, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.isGreaterThanOrEqualTo(
            columnA, columnB, self.validate_eval(assertion), hint)

    def dq_is_less_than(self, columnA, columnB, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.isLessThan(
            columnA, columnB, self.validate_eval(assertion), hint)

    def dq_is_less_than_or_equal_to(self, columnA, columnB, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.isLessThanOrEqualTo(
            columnA, columnB, self.validate_eval(assertion), hint)

    def dq_is_non_negative(self, column, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.isNonNegative(
            column, self.validate_eval(assertion), hint)

    def dq_is_positive(self, column, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.isPositive(
            column, self.validate_eval(assertion), hint)

    def dq_has_number_of_distinct_values(self, column, assertion, binningUdf, maxBins, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasNumberOfDistinctValues(
            column, self.validate_eval(assertion), binningUdf, maxBins, hint)

    def dq_has_histogram_values(self, column, assertion, binningUdf, maxBins, hint):     
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasHistogramValues(
            column, self.validate_eval(assertion), binningUdf, maxBins, hint)   

    def dq_has_pattern(self, column, pattern, assertion, name, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasPattern(
            column, pattern, self.validate_eval(assertion), name, hint) 

    def dq_has_data_type(self, column, datatype, assertion, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.hasDataType(
            column, self.validate_eval(datatype), self.validate_eval(assertion), hint) 

    def dq_kll_sketch_satisfies(self, column, assertion, kllParameters, hint):
        self.pydeequ_check_instance = self.pydeequ_check_instance.kllSketchSatisfies(
            column, self.validate_eval(assertion), self.validate_eval(kllParameters), hint) 

    def parse(self):
        # add all constraints into pydeequ check instance
        for current_check in self.user_checks:
            current_name = current_check['name']
            current_parameters = current_check['parameters']
            self.functions_map[current_name](**current_parameters)
        return self.pydeequ_check_instance