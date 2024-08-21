```csharp
namespace Project.Domain.Brands.DomainEvents
{
    public class BrandUpdatedEvent : DomainEventBase
    {
        public Brand Brand { get; }
        public DateTimeOffset Date { get; }

        public BrandUpdatedEvent(Brand brand)
        {
            Brand = brand;
            Date = DateTimeOffset.UtcNow;
        }
    }
}
```