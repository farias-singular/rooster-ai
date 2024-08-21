```csharp
namespace Project.Infrastructure.Persistence.Multitenant
{
    public class MultitenantContext : DbContext
    {
        private readonly IMediator _mediator;
        private readonly ITenantProvider _tenantProvider;

        public MultitenantContext(
            DbContextOptions<MultitenantContext> options,
            IMediator mediator,
            ITenantProvider tenantProvider)
            : base(options)
        {
            _mediator = mediator;
            _tenantProvider = tenantProvider;
        }

        public DbSet<Brand> Brands { get; set; }
    }
}
```