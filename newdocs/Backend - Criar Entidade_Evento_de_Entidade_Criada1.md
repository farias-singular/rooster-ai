```csharp
namespace Project.Domain.Brands.DomainEvents
{
    public class BrandCreatedEvent : DomainEventBase
    {
        public Brand Brand { get; }
        public DateTimeOffset Date { get; }

        public BrandCreatedEvent(Brand brand)
        {
            Brand = brand;
            Date = DateTimeOffset.UtcNow;
        }
    }
}
```