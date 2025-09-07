FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build

WORKDIR /src
COPY LoopBench.cs .

# Compila
RUN dotnet new console -n LoopApp -o . --force
RUN mv LoopBench.cs Program.cs
RUN dotnet publish -c Release -o /app

FROM mcr.microsoft.com/dotnet/runtime:8.0
WORKDIR /app
COPY --from=build /app .
CMD ["dotnet", "LoopApp.dll"]
