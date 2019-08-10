#include <stdio.h>

int main()
{
	//print welcome
	printf("Welcome to John's Simple Budget. Please note that in rent I have bundled water, trash, and sewage as that is how my personal situation is set up.\n");

	//vars for monthly income/expenses
	int income;
	int rent;
	int electric;
	int internet;
	int debt;
	int savings;
	int grocWeek;
	int groceries;
	int leftover;
	int leftweek;
	int leftday;
	int affRent;
	
	//get monthly income
	printf("Enter your total monthly income\n");

	scanf("%d", &income);

	//get monthly expenses
	printf("Enter your monthly rent: ");
	scanf("%d", &rent);

	printf("Enter your monthly electric: ");
	scanf("%d", &electric);

	printf("Enter your monthly internet: ");
	scanf("%d", &internet);

	printf("Enter your monthly debt repayments: ");
	scanf("%d", &debt);

	printf("Enter your monthly savings: ");
	scanf("%d", &savings);

	printf("Enter your weekly grocery bill: ");
	scanf("%d", &grocWeek);
	
	//calculations based on above info
	groceries = grocWeek * 4;
	leftover = income - (rent + internet + electric + debt + savings + groceries);
	leftweek = leftover/4;
	leftday = leftover/30;
	affRent = income * .3;

	printf("\n#####################################\n");
	printf("Totals\n");
	printf("#####################################\n");
	printf("Rent: $%d\n", rent);
	printf("Electric: $%d\n", electric);
	printf("Internet: $%d\n", internet);
	printf("Debt: $%d\n", debt);
	printf("Savings: $%d\n", savings);
	printf("Groceries: $%d\n", groceries);
	printf("Leftover: $%d\n", leftover);
	printf("You can also take leftover as %d$ per week\n", leftweek); 
	printf("Or alternatively $%d per day\n", leftday);

	printf("\n#####################################\n");
	printf("Additional Notes\n");
	printf("#####################################\n");
	if (affRent >= rent)
	{
		printf("Based on your income, you can afford your rent!\n");
	}	
	else 
	{
		printf("Uh oh! Your rent/mortgage is more than 1/3rd of your income! You should try to lower it\n");
	}
	
	
	return 0;




}
