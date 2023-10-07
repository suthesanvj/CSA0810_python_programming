import scipy.stats as stats
sample_mean = 91
sample_std_dev = 8 
sample_size = 30 
confidence_level = 0.85
z_score = stats.norm.ppf((1 + confidence_level) / 2)
margin_of_error = z_score * (sample_std_dev / (sample_size**0.5))
lower_limit = sample_mean - margin_of_error
upper_limit = sample_mean + margin_of_error
print(f"85% Confidence Interval for Mean Diameter: ({lower_limit:.2f} mm, {upper_limit:.2f} mm)")
