```csharp
namespace Project.Tests.Domain.Common
{
    public static partial class EntityFaker
    {
        private static Faker<Brand> FakeBrand(
            string? id = null, 
            Organization? organization = null, 
            Category? category = null, 
            string? name = null, 
            string? title = null, 
            DateTimeOffset? createdAt = null, 
            DateTimeOffset? updatedAt = null)
        {
            organization ??= RandomOrganization();
            category ??= RandomCategory();

            return new Faker<Brand>()
                .CustomInstantiator(f => Brand.Create(
                    id: id ?? f.Random.String(),
                    organization: organization,
                    category: category,
                    name: name ?? f.Random.String(),
                    title: title,
                    brandUniquenessChecker: Substitute.For<IBrandUniquenessChecker>()))
                .RuleFor(b => b.CreatedAt, f => createdAt ?? DateTimeOffset.UtcNow)
                .RuleFor(b => b.UpdatedAt, f => updatedAt ?? DateTimeOffset.UtcNow);
        }

        public static Brand RandomBrand(
            string? id = null, 
            Organization? organization = null, 
            Category? category = null, 
            string? name = null, 
            string? title = null, 
            DateTimeOffset? createdAt = null, 
            DateTimeOffset? updatedAt = null)
        {
            return FakeBrand(
                id, 
                organization,
                category,
                name,
                title,
                createdAt,
                updatedAt).Generate();
        }

        public static List<Brand> RandomBrands(int total = 10)
        {
            return FakeBrand().Generate(total);
        }
    }
}

```