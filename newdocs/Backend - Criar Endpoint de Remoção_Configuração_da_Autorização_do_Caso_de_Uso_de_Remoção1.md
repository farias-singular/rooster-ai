```csharp
namespace Project.Application.Configuration
{
    public static class MediatorExtension
    {
        public static IServiceCollection AddMediatorConfiguration(this IServiceCollection services) =>
            services.AddMediatR(cfg =>
            {
                cfg.RegisterServicesFromAssembly(Assembly.GetExecutingAssembly());

                cfg.AddBehavior<IPipelineBehavior<DeleteBrandCommand, Unit>, DeleteBrandAuthorizationBehavior>();
            });
    }
}
```