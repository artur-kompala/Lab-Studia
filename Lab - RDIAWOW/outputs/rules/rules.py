def findDecision(obj): #obj[0]: ph_range1, obj[1]: ph_range2, obj[2]: Hardness_range1, obj[3]: Hardness_range2, obj[4]: Solids_range1, obj[5]: Solids_range2, obj[6]: Chloramines_range1, obj[7]: Chloramines_range2, obj[8]: Sulfate_range1, obj[9]: Sulfate_range2, obj[10]: Conductivity_range1, obj[11]: Conductivity_range2, obj[12]: Organic_carbon_range1, obj[13]: Organic_carbon_range2, obj[14]: Trihalomethanes_range1, obj[15]: Trihalomethanes_range2, obj[16]: Turbidity_range1, obj[17]: Turbidity_range2
   # {"feature": "Solids_range1", "instances": 293, "metric_value": 0.0102, "depth": 1}
   if obj[4]>False:
      # {"feature": "Organic_carbon_range1", "instances": 163, "metric_value": 0.0085, "depth": 2}
      if obj[12]>False:
         # {"feature": "Conductivity_range1", "instances": 87, "metric_value": 0.0077, "depth": 3}
         if obj[10]>False:
            # {"feature": "Sulfate_range1", "instances": 44, "metric_value": 0.014, "depth": 4}
            if obj[8]<=False:
               # {"feature": "Hardness_range1", "instances": 23, "metric_value": 0.1375, "depth": 5}
               if obj[2]>False:
                  return 0.38461538461538464
               elif obj[2]<=False:
                  return 0
               else:
                  return 0.21739130434782608
            elif obj[8]>False:
               # {"feature": "Hardness_range1", "instances": 21, "metric_value": 0.0908, "depth": 5}
               if obj[2]<=False:
                  return 0.6666666666666666
               elif obj[2]>False:
                  return 0.1111111111111111
               else:
                  return 0.42857142857142855
            else:
               return 0.3181818181818182
         elif obj[10]<=False:
            # {"feature": "ph_range1", "instances": 43, "metric_value": 0.0165, "depth": 4}
            if obj[0]>False:
               # {"feature": "Hardness_range1", "instances": 24, "metric_value": 0.0406, "depth": 5}
               if obj[2]>False:
                  return 0.21428571428571427
               elif obj[2]<=False:
                  return 0.6
               else:
                  return 0.375
            elif obj[0]<=False:
               # {"feature": "Trihalomethanes_range1", "instances": 19, "metric_value": 0.0552, "depth": 5}
               if obj[14]>False:
                  return 0.8181818181818182
               elif obj[14]<=False:
                  return 0.375
               else:
                  return 0.631578947368421
            else:
               return 0.4883720930232558
         else:
            return 0.40229885057471265
      elif obj[12]<=False:
         # {"feature": "Sulfate_range1", "instances": 76, "metric_value": 0.018, "depth": 3}
         if obj[8]<=False:
            # {"feature": "Chloramines_range1", "instances": 42, "metric_value": 0.1241, "depth": 4}
            if obj[6]>False:
               # {"feature": "Conductivity_range1", "instances": 21, "metric_value": 0.0481, "depth": 5}
               if obj[10]<=False:
                  return 0.45454545454545453
               elif obj[10]>False:
                  return 0.1
               else:
                  return 0.2857142857142857
            elif obj[6]<=False:
               return 0
            else:
               return 0.14285714285714285
         elif obj[8]>False:
            # {"feature": "Hardness_range1", "instances": 34, "metric_value": 0.0163, "depth": 4}
            if obj[2]<=False:
               # {"feature": "Turbidity_range1", "instances": 20, "metric_value": 0.0394, "depth": 5}
               if obj[16]<=False:
                  return 0.3076923076923077
               elif obj[16]>False:
                  return 0.7142857142857143
               else:
                  return 0.45
            elif obj[2]>False:
               # {"feature": "Conductivity_range1", "instances": 14, "metric_value": 0.196, "depth": 5}
               if obj[10]>False:
                  return 0
               elif obj[10]<=False:
                  return 0.5
               else:
                  return 0.21428571428571427
            else:
               return 0.35294117647058826
         else:
            return 0.23684210526315788
      else:
         return 0.32515337423312884
   elif obj[4]<=False:
      # {"feature": "Hardness_range1", "instances": 130, "metric_value": 0.025, "depth": 2}
      if obj[2]<=False:
         # {"feature": "Sulfate_range1", "instances": 69, "metric_value": 0.031, "depth": 3}
         if obj[8]<=False:
            # {"feature": "Chloramines_range1", "instances": 39, "metric_value": 0.0061, "depth": 4}
            if obj[6]>False:
               # {"feature": "Organic_carbon_range1", "instances": 21, "metric_value": 0.0258, "depth": 5}
               if obj[12]>False:
                  return 0.16666666666666666
               elif obj[12]<=False:
                  return 0.4444444444444444
               else:
                  return 0.2857142857142857
            elif obj[6]<=False:
               # {"feature": "ph_range1", "instances": 18, "metric_value": 0.0077, "depth": 5}
               if obj[0]>False:
                  return 0.2222222222222222
               elif obj[0]<=False:
                  return 0.1111111111111111
               else:
                  return 0.16666666666666666
            else:
               return 0.23076923076923078
         elif obj[8]>False:
            # {"feature": "ph_range1", "instances": 30, "metric_value": 0.0265, "depth": 4}
            if obj[0]<=False:
               # {"feature": "Chloramines_range1", "instances": 17, "metric_value": 0.0158, "depth": 5}
               if obj[6]<=False:
                  return 0.7692307692307693
               elif obj[6]>False:
                  return 0.5
               else:
                  return 0.7058823529411765
            elif obj[0]>False:
               # {"feature": "Organic_carbon_range1", "instances": 13, "metric_value": 0.1886, "depth": 5}
               if obj[12]>False:
                  return 0.625
               elif obj[12]<=False:
                  return 0
               else:
                  return 0.38461538461538464
            else:
               return 0.5666666666666667
         else:
            return 0.37681159420289856
      elif obj[2]>False:
         # {"feature": "ph_range1", "instances": 61, "metric_value": 0.0211, "depth": 3}
         if obj[0]<=False:
            # {"feature": "Organic_carbon_range1", "instances": 35, "metric_value": 0.0132, "depth": 4}
            if obj[12]>False:
               # {"feature": "Turbidity_range1", "instances": 18, "metric_value": 0.0105, "depth": 5}
               if obj[16]>False:
                  return 0.8
               elif obj[16]<=False:
                  return 0.625
               else:
                  return 0.7222222222222222
            elif obj[12]<=False:
               # {"feature": "Turbidity_range1", "instances": 17, "metric_value": 0.1558, "depth": 5}
               if obj[16]<=False:
                  return 1
               elif obj[16]>False:
                  return 0.6666666666666666
               else:
                  return 0.8823529411764706
            else:
               return 0.8
         elif obj[0]>False:
            # {"feature": "Turbidity_range1", "instances": 26, "metric_value": 0.0407, "depth": 4}
            if obj[16]<=False:
               # {"feature": "Chloramines_range1", "instances": 14, "metric_value": 0.0568, "depth": 5}
               if obj[6]>False:
                  return 0.5714285714285714
               elif obj[6]<=False:
                  return 0.14285714285714285
               else:
                  return 0.35714285714285715
            elif obj[16]>False:
               # {"feature": "Conductivity_range1", "instances": 12, "metric_value": 0.2289, "depth": 5}
               if obj[10]>False:
                  return 1
               elif obj[10]<=False:
                  return 0.4
               else:
                  return 0.75
            else:
               return 0.5384615384615384
         else:
            return 0.6885245901639344
      else:
         return 0.5230769230769231
   else:
      return 0.4129692832764505
