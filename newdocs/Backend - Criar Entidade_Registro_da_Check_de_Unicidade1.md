```csharp
namespace Project.API.Configuration
{
    public static class InfrastructureExtension
    {
        private static IServiceCollection AddEntityFactory(this IServiceCollection services)
        {
            services.AddTransient<IBrandUniquenessChecker, BrandUniquenessChecker>();

            return services;
        }
    }
}
```