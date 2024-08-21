```csharp
namespace Project.API.Configuration
{
    public static class InfrastructureExtension
    {
        private static IServiceCollection AddRepositories(this IServiceCollection services)
        {
            services.AddScoped<IBrandRepository, BrandRepository>();

            return services;
        }
    }
}
```