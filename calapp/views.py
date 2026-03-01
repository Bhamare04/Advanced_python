from django.shortcuts import render


def calculator_view(request):

    result = ""
    num1 = ""
    num2 = ""

    if request.method == "POST":

        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        op = request.POST.get("op")

        try:
            n1 = float(num1)
            n2 = float(num2)

            if op == "add":
                result = n1 + n2
            elif op == "sub":
                result = n1 - n2
            elif op == "mul":
                result = n1 * n2
            elif op == "div":
                if n2 != 0:
                    result = n1 / n2
                else:
                    result = "Cannot divide by zero"

        except:
            result = "Invalid input"

    return render(request, "calculator.html", {
        "result": result,
        "num1": num1,
        "num2": num2
    })